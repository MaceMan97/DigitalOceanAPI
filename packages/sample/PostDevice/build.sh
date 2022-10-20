#!/bin/bash

set -e

virtualenv virtualenv
source virtualenv/bin/activate
pip install -m requirements.txt
deactivate