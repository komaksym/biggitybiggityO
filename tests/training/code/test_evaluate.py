import pytest
from src.training.code.scripts.evaluate import hc_score, compute_metrics
import torch
import numpy as np


@pytest.mark.parametrize(
        "y_true, preds, result",
        [
            (np.array([0, 1, 2, 4, 1]), 
             np.array([0, 4, 2, 1, 3]),
             np.float64(0.22857142857142856)),

             (np.array([1, 5, 2, 5, 6, 0, 3, 5]),
             np.array([2, 3, 1, 0, 4, 5, 4, 5]),
             np.float64(0.30357142857142855))
        ]
)
def test_hc_score(y_true, preds, result):
    assert hc_score(y_true, preds) == result

    # Not equal lengths, should raise AssertionError
    with pytest.raises(AssertionError):
        hc_score(np.array([0, 4, 2, 5, 3]), np.array([4, 2, 1, 3])) 
    

def test_compute_metrics():
    pass