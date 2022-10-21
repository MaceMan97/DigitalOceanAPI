#!/bin/bash

set -e

virtualenv --without-pip virtualenv
pip install mysql-connector-python