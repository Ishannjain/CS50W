FROM python:3
COPY . /usrc/src/app
WORKDIR /usrc/src/app
RUN pip install -r requirements.txt
CHD ["python3","manage.py","runserver","0.0.0.8000"]