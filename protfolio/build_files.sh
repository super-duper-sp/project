echo " BUILD START"
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
echo " BUILD END"


app = application

ALLOWED_HOSTS = ['.vercel.app', '.now.sh']


STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT  = BASE_DIR / "staticfiles"

