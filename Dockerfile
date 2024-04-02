ARG image_tag=0.0.1
FROM python:3.12-slim
LABEL authors="Fredly"

RUN apt-get update && apt-get install -y \
    build-essential zlib1g-dev libjpeg-dev\
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN pip install --no-cache -r requirements.txt
ENTRYPOINT ["python", "main.py"]
CMD ["--mode", "arg1"]