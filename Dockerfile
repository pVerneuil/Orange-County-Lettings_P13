FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1
ENV PORT 8000
ENV TOKEN_SENTRY = ${TOKEN_SENTRY}

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

EXPOSE $PORT

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT