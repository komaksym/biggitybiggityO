#!/bin/bash

# Activate venv and install packages
source bin/activate
pip install -r requirements.txt

# Set up git to be able to push to github
git remote set-url origin  git@github.com:komaksym/biggitybiggityO.git
git config --global user.email "kovalmaksym2@gmail.com"
git config --global user.name "komaksym"

# Install oh-my-bash for ga gc gd commands
bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"

# Training script
accelerate launch --config_file src/training/code/scripts/configs/fsdp_config.yaml src/training/code/scripts/train.py