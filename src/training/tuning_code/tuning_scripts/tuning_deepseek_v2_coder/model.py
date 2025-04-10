#!pip install pandas scikit-learn peft datasets tensorboardX numba bitsandbytes

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from transformers import AutoModel, AutoTokenizer, AutoModelForSequenceClassification, \
                         TrainingArguments, Trainer, DataCollatorWithPadding, BitsAndBytesConfig
from peft import LoraConfig, get_peft_model
from datasets import load_dataset, Dataset
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, f1_score, make_scorer
import os
import torch
import torch.nn as nn
import pdb


DATASET_PATHS = {
    "local": {
        "train": "../../datasets/train_set.csv",
        "test": "../../datasets/test_set.csv"
    },
    "local_two": {
        "train": "train_set.csv",
        "test": "test_set.csv"
    },
    "local_three": {
        "train": "drive/MyDrive/fine_tuning/train_set.csv",
        "test": "drive/MyDrive/fine_tuning/test_set.csv"
    },

    "kaggle": {
        "train": "/kaggle/input/python-codes-time-complexity/train_set.csv",
        "test": "/kaggle/input/python-codes-time-complexity/test_set.csv"
    }
}

def upload_datasets(dataset_paths=DATASET_PATHS):
    for path in dataset_paths:
        if os.path.exists(dataset_paths[path]['train']) and os.path.exists(dataset_paths[path]['test']):
            return dataset_paths[path]['train'], dataset_paths[path]['test']

    return FileNotFoundError(f"Datasets do not exist in the current paths: {dataset_paths}")


train_set_path, test_set_path = upload_datasets()


# # Metrics

# ### Ordering labels by Hierarchy


LABELS_HIERARCHY = {
    'constant': 1,
    'logn': 2,
    'linear': 3,
    'nlogn': 4,
    'quadratic': 5,
    'cubic': 6,
    'np': 7
}

N_CLASSES = len(LABELS_HIERARCHY)


# # Dataset uploading

# In[5]:


train_set = load_dataset("csv", data_files=train_set_path)['train']
test_set = load_dataset("csv", data_files=test_set_path)['train']

train_labels = train_set['complexity']
test_labels = test_set['complexity']


# # Evaluating

# ### Writing the custom metric *Hierarchy Complexity Score*

# In[6]:


def hc_score(y_true, y_pred, n_classes=N_CLASSES):
    assert len(y_true) == len(y_pred), f"The amount of y_true labels: {len(y_true)} does not equal to the amount of y_pred: {len(y_pred)}."

    n_samples = len(y_true)

    return (np.sum(np.abs(y_pred - y_true)) / n_classes) / n_samples


# ## Computing metrics

# In[7]:


def compute_metrics(eval_preds):
    logits, labels = eval_preds
    preds = np.argmax(logits[0], axis=-1) if isinstance(logits, tuple) else np.argmax(logits, axis=-1)

    # Calculate accuracy
    accuracy = accuracy_score(labels, preds)
    # Calculate F-1 Macro
    f1_macro_score = f1_score(labels, preds, average='macro')
    # Calculate Hierarchy Score
    hierarchy_score = hc_score(labels, preds)

    return {
        "accuracy": accuracy,
        "f1_macro": f1_macro_score,
        "hierarchy_score": hierarchy_score
    }


# # Tokenizing

# ## Label tokenizing

# In[8]:


labelEncoder = LabelEncoder()
labelEncoder.fit(train_set['complexity'])


# ## Feature tokenizing

# In[9]:


def tokenize_data(samples, tokenizer):
    tokenized = tokenizer(samples['code'], truncation=True, padding=True, max_length=512)
    tokenized['labels'] = labelEncoder.transform(samples['complexity'])
    return tokenized


def set_tokenizer(checkpoint):
    try:
        tokenizer = AutoTokenizer.from_pretrained(checkpoint, pad_token="<pad>")
    except Exception as e:
        print(f"Failed to load {checkpoint}: {e}")
        checkpoint = "-".join(checkpoint.split("-")[:2])
        tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        print(f"Falling back to {checkpoint}")

    X_train = train_set.map(
        lambda x: tokenize_data(x, tokenizer),
        batched=True,
        remove_columns=train_set.column_names
    )
    X_eval = test_set.map(
        lambda x: tokenize_data(x, tokenizer),
        batched=True,
        remove_columns=test_set.column_names
    )

    # Optional: Verify columns
    print("X_train columns:", X_train.column_names)
    print("X_eval columns:", X_eval.column_names)

    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
    return tokenizer, data_collator, X_train, X_eval

# # Model

# ## Device

# In[10]:


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# ## Checkpoint

# In[11]:


checkpoint = "deepseek-ai/DeepSeek-Coder-V2-Lite-Base"


# ## Quantizing

# In[12]:


# Configure 4-bit quantization
quant_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type = 'nf4',
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_storage=torch.bfloat16

)


# ## Model loading

# In[13]:


def set_model(checkpoint, tokenizer):
    model = AutoModel.from_pretrained(checkpoint, torch_dtype='bfloat16', num_labels=7,
                                      trust_remote_code=True, quantization_config=quant_config)
    # Configuring padding token in case is absent
    model.config.pad_token_id = tokenizer.pad_token_id
    # As well, as resizing the embeddings to accomodate the new *pad* token
    model.resize_token_embeddings(len(tokenizer))


    return model


# ## Classifier head

# In[14]:


from transformers import AutoModelForCausalLM, AutoConfig, PreTrainedModel
from transformers.modeling_outputs import SequenceClassifierOutput

class DeepseekV2ForSequenceClassification(PreTrainedModel):
    config_class = AutoConfig

    def __init__(self, base_model, config):
        super().__init__(config)
        self.num_labels = config.num_labels
        self.model = base_model

        self.dense = nn.Linear(config.hidden_size, config.num_labels, device=self.model.device, dtype=config.torch_dtype)
        # Initialize weights and apply final processing
        self.post_init()

    def get_input_embeddings(self):
        return self.model.embed_tokens

    def forward(self, input_ids=None, attention_mask=None, labels=None, *args, **kwargs):
        # Filter out unexpected keyword arguments for the base model
        model_kwargs = {k: v for k, v in kwargs.items() if k in [
            'past_key_values', 'use_cache', 'output_attentions', 
            'output_hidden_states', 'return_dict'
        ]}

        # Call the base model with only the expected arguments
        outputs = self.model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            *args,
            **model_kwargs
        )
        hidden_states = outputs.last_hidden_state
        logits = self.dense(hidden_states)

        # Batch size
        if input_ids is not None:
            batch_size = input_ids.shape[0]

        # If padding token id is not configured and the batch size is > 1
        if self.config.pad_token_id is None and batch_size != 1:
            raise ValueError("Cannot handle batch sizes > 1 if no padding token is defined.")
        # If padding token id is not configured
        if self.config.pad_token_id is None:
            last_non_pad_token = -1
        # if encoded inputs exist => find the last non padded token to pool data from
        elif input_ids is not None:
            non_pad_mask = (input_ids != self.config.pad_token_id).to(logits.device, dtype=torch.int32)
            token_indices = torch.arange(input_ids.shape[-1], device=logits.device, dtype=torch.int32)
            last_non_pad_token = (token_indices * non_pad_mask).argmax(-1)

        # Pooling logits from the last non padded token across the batches
        pooled_logits = logits[torch.arange(batch_size, device=logits.device), last_non_pad_token]

        # Calculating loss if labels are provided
        loss = None
        if labels is not None:
            loss = self.loss_function(logits=logits, labels=labels, pooled_logits=pooled_logits, config=self.config)

        return SequenceClassifierOutput(loss=loss, logits=pooled_logits)


# ## Loading tokenizer and model

# In[15]:


#tokenizer, data_collator, train_set, eval_set = set_tokenizer(checkpoint)
#base_model = set_model(checkpoint)


# In[16]:


#model = DeepseekV2ForSequenceClassification(base_model, base_model.config)


# # LoRA

# #### Check module names in the model to specify them in *target_modules* param

# model = set_model(checkpoint)
# for name, module in model.named_modules():
#     print(name)

# ## LoRA config

# In[17]:


config = LoraConfig(
    r=64,
    lora_alpha=16,
    lora_dropout=0.1,
    bias='none',
    task_type = "SEQ_CLS",
    target_modules = 'all-linear',
)

#model = get_peft_model(model=model, peft_config=config)
#model.print_trainable_parameters()


# ### Flash the drive

# !rm -rf training_results

# # Trainer Args

# In[18]:


def set_training_args(checkpoint, batch_size=16):
    training_args = TrainingArguments(output_dir=f"training_results/{checkpoint}/",
                                      eval_strategy="epoch",
                                      save_strategy="epoch",
                                      logging_strategy="epoch",
                                      #learning_rate=2e-4, # Testing
                                      bf16=True,
                                      report_to='tensorboard',
                                      num_train_epochs=3,
                                      warmup_steps=100, # Testing
                                      per_device_train_batch_size=batch_size,
                                      per_device_eval_batch_size=batch_size,
                                      gradient_accumulation_steps = 1,
                                      # Testing
                                      load_best_model_at_end=True,
                                      remove_unused_columns=False,
                                     )
    return training_args