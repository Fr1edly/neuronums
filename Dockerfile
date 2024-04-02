ARG image_tag=0.0.1
FROM python:3.12.2-alpine3.18
LABEL authors="Fredly"
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]
CMD ["--mode", "arg1"]