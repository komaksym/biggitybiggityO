import pytest
from src.training.code.scripts.evaluate import hc_score, compute_metrics
import torch
import numpy as np
from transformers import EvalPrediction


@pytest.mark.parametrize(
    "y_true, preds, result",
    [
        (np.array([0, 1, 2, 4, 1]), np.array([0, 4, 2, 1, 3]), np.float64(0.22857142857142856)),
        (
            np.array([1, 5, 2, 5, 6, 0, 3, 5]),
            np.array([2, 3, 1, 0, 4, 5, 4, 5]),
            np.float64(0.30357142857142855),
        ),
    ],
)
def test_hc_score(y_true, preds, result):
    assert hc_score(y_true, preds) == result

    # Not equal lengths, should raise AssertionError
    with pytest.raises(AssertionError):
        hc_score(np.array([0, 4, 2, 5, 3]), np.array([4, 2, 1, 3]))


@pytest.fixture
def mock_eval_preds():
    logits = np.array(
        [
            [-0.14160156, 0.37304688, 2.59375, 0.22265625, 0.4140625, -1.390625, -1.5546875],
            [-0.44921875, 0.13769531, 0.35351562, 0.38085938, 0.07128906, -0.4765625, -0.23339844],
            [-0.59375, 0.04052734, 3.265625, 0.578125, 0.6171875, -1.421875, -1.890625],
            [-0.453125, 0.12207031, 0.47851562, 0.34570312, 0.09960938, -0.33398438, -0.38085938],
            [0.24902344, 0.7890625, 0.328125, -0.09179688, -0.296875, -0.41796875, -0.53125],
            [-0.07617188, 0.66015625, 0.10449219, 0.02734375, -0.2578125, -0.19726562, -0.30859375],
            [-0.55859375, 0.05859375, 3.34375, 0.2578125, 0.703125, -1.3671875, -1.6953125],
            [-0.26953125, 0.21875, 1.921875, 0.06298828, 0.21582031, -1.0625, -1.453125],
            [-0.671875, -0.03759766, 3.078125, 0.55859375, 0.8828125, -1.484375, -1.75],
            [-0.80078125, -0.10449219, 3.34375, 1.0625, 0.671875, -1.734375, -2.03125],
        ]
    )

    labels = np.array([2, 2, 2, 3, 1, 6, 2, 2, 2, 2])

    return EvalPrediction(predictions=logits, label_ids=labels)


@pytest.fixture
def expected_metrics():
    return {
        "accuracy": 0.7,
        "f1_macro": 0.38095238095238093,
        "recall_score": {
            "constant": np.float64(0.0),
            "logn": np.float64(1.0),
            "linear": np.float64(0.86),
            "nlogn": np.float64(0.0),
            "quadratic": np.float64(0.0),
            "cubic": np.float64(0.0),
            "np": np.float64(0.0),
        },
        "hierarchy_score": np.float64(0.1),
    }


def test_compute_metrics(mock_eval_preds, expected_metrics):
    got_metrics = compute_metrics(mock_eval_preds)

    assert got_metrics == expected_metrics
