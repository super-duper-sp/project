#!/bin/bash

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# Install project dependencies within the virtual environment
pip install -r requirements.txt

# Run any other necessary build steps or commands
# For example:
# python manage.py collectstatic
# python manage.py migrate

# Deactivate the virtual environment when done
deactivate


