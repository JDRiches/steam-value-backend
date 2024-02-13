FROM python:3.11-buster

RUN pip install poetry==1.7.1

WORKDIR /app

COPY pyproject.toml poetry.lock ./

COPY main.py ./
COPY SteamAPICaller.py ./


RUN poetry install 

COPY clean_app_list.json ./

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

 