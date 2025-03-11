#!/bin/bash
set -e

# Enable virtual environment
if [ ! -d venv ]; then
	python3 -m venv venv
fi
. venv/bin/activate

# Install requirements
python3 -m pip install -r requirements.txt
