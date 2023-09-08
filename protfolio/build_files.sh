# build_files.sh
python -m venv venv
venv\Scripts\activate
source venv/bin/activate
pip install -r requirements.txt
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate



