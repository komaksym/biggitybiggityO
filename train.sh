#!/bin/bash

# Training script
accelerate launch --config_file src/training/code/scripts/configs/fsdp_config.yaml src/training/code/scripts/train.py