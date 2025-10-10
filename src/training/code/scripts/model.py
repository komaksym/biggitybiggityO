import torch
import torch.nn as nn
from accelerate import PartialState
from configs.config import checkpoint
from data import tokenizer
from peft import LoraConfig, get_peft_model
from transformers import (
    AutoConfig,
    AutoModel,
    AutoModelForSequenceClassification,
    BitsAndBytesConfig,
    PreTrainedModel,
)
from transformers.modeling_outputs import SequenceClassifierOutput
from evaluate import N_CLASSES

# Bitsandbytes (Quantization)
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_storage=torch.bfloat16,
)


# Model loading
def set_model(checkpoint, tokenizer, ModelType=AutoModel):
    # Setup bitsandbytes quantization config
    quant_config = bnb_config

    # Load a pretrained model
    model = ModelType.from_pretrained(
        checkpoint,
        torch_dtype="auto",
        num_labels=N_CLASSES,
        trust_remote_code=True,
        device_map=PartialState().process_index,
        quantization_config=quant_config,
        attn_implementation="flash_attention_2",  # Only for newer models
    )

    # Accomodating the size of the token embeddings for the potential missing <pad> token
    model.resize_token_embeddings(len(tokenizer), mean_resizing=False)

    # Passing the pad token id to the model config
    model.config.pad_token_id = tokenizer.pad_token_id
    return model


# Custom classifier head
class DeepseekV2ForSequenceClassification(PreTrainedModel):
    config_class = AutoConfig

    def __init__(self, base_model, config):
        super().__init__(config)
        self.num_labels = config.num_labels
        self.model = base_model

        self.dense = nn.Linear(config.n_embd, config.num_labels, bias=False, dtype=self.model.dtype)

        # Initialize weights and apply final processing
        self.post_init()

    def get_input_embeddings(self):
        return self.model.config.n_embd

    def forward(self, input_ids=None, attention_mask=None, labels=None, *args, **kwargs):
        outputs = self.model(input_ids, attention_mask)

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
            loss = self.loss_function(
                logits=logits,
                labels=labels,
                pooled_logits=pooled_logits,
                config=self.config,
            )

        return SequenceClassifierOutput(loss=loss, logits=pooled_logits)


# LoRA config
peft_config = LoraConfig(
    r=32,
    lora_alpha=64,
    # target_modules = ['q_proj', 'v_proj'], # Qwen
    target_modules="all-linear",  # Heavy, universal
    lora_dropout=0.1,
    bias="none",
    task_type="SEQ_CLS",  # might not work with this on
)


model = set_model(checkpoint, tokenizer, AutoModelForSequenceClassification)

# model = DeepseekV2ForSequenceClassification(model, model.config)
model = get_peft_model(model=model, peft_config=peft_config)

# print(f"Model: {model}")
# print(f"Model config: {model.config}")
