FROM ubuntu:18.04 AS builder



RUN mkdir -p /build/src && \
    mkdir -p /build/bin && \
    apt-get update && \
    apt-get install python3-dev python3 python3-venv python-pip -y

COPY src /build/src
COPY bin /build/bin
COPY setup.py /build/setup.py
COPY pg2009.txt /build/pg2009.txt

WORKDIR /build

RUN pip install -e .

FROM builder

RUN mkdir -p /tests

COPY tests /tests

WORKDIR /tests

RUN chmod +x *.sh;./test_top_ten.sh
