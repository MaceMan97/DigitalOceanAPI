#!/bin/bash

virtualenv envname
pip install requirements.txt --target venv/lib/python3.30/site-packages

pip list

deactivate