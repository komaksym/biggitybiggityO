#!/bin/bash

source bin/activate
pip install -r requirements.txt

git remote set-url origin  git@github.com:komaksym/biggitybiggityO.git
git config --global user.email "kovalmaksym2@gmail.com"
git config --global user.name "komaksym"

bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"

accelerate launch --config_file src/training/code/scripts/configs/fsdp_config.yaml src/training/code/scripts/train.py