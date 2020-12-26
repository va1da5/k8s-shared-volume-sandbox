FROM python:3.8.7-slim-buster

ENV PORT=8000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "/bin/sh" ]
CMD [ "-c", "gunicorn --bind 0.0.0.0:$PORT wsgi:app --threads 2 --workers 2" ]