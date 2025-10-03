import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from data import eval_set, train_set
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, f1_score, recall_score
from sklearn.preprocessing import LabelEncoder
from transformers import AutoTokenizer, DataCollatorWithPadding, TrainerCallback
from dotenv import load_dotenv
import os
import mlflow


def setup_mlflow():
    # To not hang for an hour if no connection could be established
    mlflow.environment_variables.MLFLOW_HTTP_REQUEST_TIMEOUT = 10

    # Fetch secrets from .env
    #load_dotenv()

    #username = os.getenv("MLFLOW_NGROK_USERNAME")
    #password = os.getenv("MLFLOW_NGROK_PASSWORD")
    #uri = os.getenv("MLFLOW_NGROK_URI")

    username = os.environ["MLFLOW_NGROK_USERNAME"]
    password = os.environ["MLFLOW_NGROK_PASSWORD"]
    uri = os.environ["MLFLOW_NGROK_URI"]

    # Connect
    mlflow.set_tracking_uri(f"https://{username}:{password}@{uri}")

    # Name the experiment
    mlflow.set_experiment("Dry runs /w default hyperparams & loss function")



LABELS_HIERARCHY = {"constant": 1, "logn": 2, "linear": 3, "nlogn": 4, "quadratic": 5, "cubic": 6, "np": 7}

N_CLASSES = len(LABELS_HIERARCHY)


# Hierarchy score
def hc_score(y_true, y_pred, n_classes=N_CLASSES):
    assert len(y_true) == len(y_pred), (
        f"The amount of y_true labels: {len(y_true)} does not equal to the amount of y_pred: {len(y_pred)}."
    )

    n_samples = len(y_true)

    return (np.sum(np.abs(y_pred - y_true)) / n_classes) / n_samples


def compute_metrics(eval_preds):
    # Make preds & labels global for access in callbacks
    global last_preds, last_labels

    logits, labels = eval_preds
    preds = np.argmax(logits[0], axis=-1) if isinstance(logits, tuple) else np.argmax(logits, axis=-1)

    # Save for callbacking
    last_preds, last_labels = preds, labels

    # Calculate accuracy
    accuracy = accuracy_score(y_true=labels, y_pred=preds)

    # Calculate F-1 Macro
    f1_macro_score = f1_score(y_true=labels, y_pred=preds, average="macro")

    # Calculate per-class recall
    recall_scores = recall_score(
        y_true=labels, y_pred=preds, average=None, labels=[0, 1, 4, 5, 2, 3, 6]
    )  # reorder labels here because of how labelEncoder encodes the labels in not complexity-wise ascending order
    recall_per_class = {}

    # Zip label: score into a dict
    for label, score in zip(LABELS_HIERARCHY.keys(), recall_scores):
        recall_per_class[label] = np.round(score, 2)

    # Calculate Hierarchy Score
    hierarchy_score = hc_score(y_true=labels, y_pred=preds)

    return {
        "accuracy": accuracy,
        "f1_macro": f1_macro_score,
        "recall_score": recall_per_class,
        "hierarchy_score": hierarchy_score,
    }


class ConfusionMatrixCallback(TrainerCallback):
    def on_evaluate(self, args, state, control, **kwargs):
        if last_preds is not None:
            # Calculate confusion matrix
            disp = ConfusionMatrixDisplay.from_predictions(
                y_true=last_labels,
                y_pred=last_preds,
                labels=[
                    0,
                    1,
                    4,
                    5,
                    2,
                    3,
                    6,
                ],  # reorder labels here because of how labelEncoder encodes the labels in not complexity-wise ascending order
                display_labels=[
                    "O(1)",
                    "O(logn)",
                    "O(n)",
                    "O(nlogn)",
                    "O(n^2)",
                    "O(n^3)",
                    "np",
                ],
            )
            # Get fig
            fig = disp.figure_

            # Make slightly wider to fit xtick labels
            fig.set_size_inches(10, 5)
            fig.tight_layout()

            # Save as png and Log to MLFlow
            fig.savefig("confusion_matrix.png")
            # Close and unregister, so that it doesn't print
            plt.close(fig)
            mlflow.log_artifact("confusion_matrix.png")


class RecallScoreCallback(TrainerCallback):
    def on_evaluate(self, args, state, control, **kwargs):
        # Parse recall scores
        recall_scores = kwargs["metrics"]["eval_recall_score"]

        # Create a barplot
        ax = sns.barplot(
            x=np.array(list(recall_scores.keys())),
            y=np.array(list(recall_scores.values())),
        )
        # Add labels
        ax.set_xlabel(xlabel="Complexity", labelpad=20, fontsize=14)
        ax.set_ylabel(ylabel="Recall score", labelpad=20, fontsize=14)

        # Save as png and log to MLFLow
        fig = ax.get_figure()
        fig.savefig("recall_per_score.png")
        # Close and unregister, so that it doesn't print
        plt.close(fig)
        mlflow.log_artifact("recall_per_score.png")


def tokenize_data(data, tokenizer):
    # Tokenizing
    tokenized = tokenizer(
        data["code"],
        truncation=True,
        max_length=512,
    )
    tokenized["labels"] = labelEncoder.transform(data["complexity"])
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
        remove_columns=train_set.column_names,
    )
    X_eval = eval_set.map(
        lambda x: tokenize_data(x, tokenizer),
        batched=True,
        remove_columns=eval_set.column_names,
    )

    # Data Collator
    tokenizer.padding_side = "left"
    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
    return tokenizer, data_collator, X_train, X_eval
