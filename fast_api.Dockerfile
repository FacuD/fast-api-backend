FROM python:3.10

RUN apt-get update

WORKDIR /app
COPY requirements.txt /app/

ENV PYTHONPATH "${PYTHONPATH}:/app/app"

RUN pip install -r requirements.txt

COPY . /app/

# WORKDIR /app/app

EXPOSE 8000
# CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0"]