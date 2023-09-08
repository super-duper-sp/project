# build_files.sh

# Define the path to your virtual environment
VENV_DIR="god"

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

pip install -r requirements.txt
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate



