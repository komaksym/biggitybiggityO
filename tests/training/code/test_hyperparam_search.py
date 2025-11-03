from src.training.code.scripts.hyperparam_search import objective
import optuna
from optuna.trial import FrozenTrial
import torch
import pytest


support = torch.cuda.is_available() and torch.cuda.is_bf16_supported()

@pytest.mark.skipif(
    not support, reason="Full hyperparameter search requires a GPU"
)
def test_objective():
    study = optuna.create_study(study_name="test_hyperparam_search", direction="maximize", load_if_exists=True)
    study.optimize(objective, n_trials=1)

    assert isinstance(study.best_trial, FrozenTrial)
