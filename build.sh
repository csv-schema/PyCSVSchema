#!/usr/bin/env bash

pyenv install -s 3.7.4
virtualenv -p ~/.pyenv/versions/3.7.4/bin/python --clear --always-copy --no-site-packages venv

source venv/bin/activate
pip3 install -r requirements.txt
deactivate
