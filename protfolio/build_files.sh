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

# Remove the virtual environment to reduce deployment size
rm -rf venv

# Create a .vercelignore file to exclude unnecessary files and directories
echo -e "venv/\n*.pyc\n*.pyo\n__pycache__/" > .vercelignore

# Continue with the deployment process
