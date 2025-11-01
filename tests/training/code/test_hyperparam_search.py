from src.training.code.scripts.hyperparam_search import objective
from src.training.code.scripts.data import set_tokenizer, label2id
from src.training.code.scripts.train import setup_model, load_data, preprocess_data
from src.training.code.scripts.configs.config import checkpoint, DATASET_PATHS
import optuna
from optuna.trial import FrozenTrial
import torch
import pytest


support = torch.cuda.is_available() and torch.cuda.is_bf16_supported()

@pytest.mark.skipif(
    not support, reason="Full hyperparameter search requires a GPU"
)
def test_objective():
    # Set up tokenizer
    tokenizer, data_collator = set_tokenizer(checkpoint)

    # Prep the data
    train_set, eval_set = load_data(DATASET_PATHS)
    # Preprocess the data
    train_set, eval_set = preprocess_data(train_set, eval_set, tokenizer, label2id)

    # Setup model
    model = setup_model(tokenizer, checkpoint)

    study = optuna.create_study(study_name="test_hyperparam_search", direction="maximize", load_if_exists=True)
    study.optimize(objective, n_trials=1)

    assert isinstance(study.best_trial, FrozenTrial)
