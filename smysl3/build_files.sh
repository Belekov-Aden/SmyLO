# build_files.sh
python3.10 -m venv env
env\Scripts\activate.bat
pip install -r requirements.txt
python3.10 manage.py collectstatic