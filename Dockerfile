FROM ubuntu:18.04 AS builder



RUN mkdir -p /build/src && \
    mkdir -p /build/bin && \
    apt-get update && \
    apt-get install python3-dev python3 python3-venv python-pip -y

COPY src /build/src
COPY bin /build/bin
COPY setup.py /build/setup.py

WORKDIR /build

RUN pip install -e .

FROM builder

WORKDIR /build/src

RUN python */test_*.py

FROM builder

WORKDIR /

CMD echo 'Usage: mount volumes with desired files, and run "phrases file1.txt file2.txt"'
