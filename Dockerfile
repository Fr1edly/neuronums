FROM python:3.12
LABEL authors="Fredly"
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]
CMD ["--mode", "run"]