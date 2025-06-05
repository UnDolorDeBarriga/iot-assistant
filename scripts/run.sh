#!/bin/bash
set -e

# Activate the virtual environment
source .venv/bin/activate

# Run main
python3 assistant/main.py
