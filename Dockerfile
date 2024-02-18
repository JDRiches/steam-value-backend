FROM python:3.11-buster

RUN pip install poetry==1.7.1

WORKDIR /app

COPY src ./src


RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r  requirements.txt


COPY clean_app_list.json ./

EXPOSE 8080

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--port=8080"]

 