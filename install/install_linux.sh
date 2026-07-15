#!/bin/bash

echo "Installing Jarvis AI Employee"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "Installation complete"