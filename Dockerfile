FROM ubuntu:20.04

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    vim \
    && rm -rf /var/lib/apt/lists/*

COPY ./ /app

RUN pip3 install --no-cache-dir -r requirements.txt
