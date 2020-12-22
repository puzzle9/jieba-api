FROM python:3.7-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple && pip config set install.trusted-host mirrors.aliyun.com
RUN pip install -r requirements.txt
COPY app.py app.py
CMD ["gunicorn",  "-w", "4", "--bind", "0.0.0.0:5000", "app:app" ]