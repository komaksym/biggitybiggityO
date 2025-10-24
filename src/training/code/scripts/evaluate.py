import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, f1_score, recall_score
from transformers import TrainerCallback
import mlflow

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
        y_true=labels, y_pred=preds, average=None, labels=[1, 2, 3, 4, 5, 6, 7]
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
                labels=[1, 2, 3, 4, 5, 6, 7],  # reorder labels here because of how labelEncoder encodes the labels in not complexity-wise ascending order
                display_labels=[
                    "O(1)",
                    "O(logn)",
                    "O(n)",
                    "O(nlogn)",
                    "O(n^2)",
                    "O(n^3)",
                    "O(2^n)",
                    "O(n!)",
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
