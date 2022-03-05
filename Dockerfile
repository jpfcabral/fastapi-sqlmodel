FROM python:3

EXPOSE 8000

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./src /app/

WORKDIR /app

CMD uvicorn main:app --host 0.0.0.0 --port 8000 --log-config=./logs/log_config.yaml --reload