FROM nvidia/cuda:12.1.1-runtime-ubuntu22.04

WORKDIR /code

RUN apt-get update && apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*
RUN python3 -m pip install --upgrade pip
RUN ln -s /usr/bin/python3 /usr/bin/python

COPY ./uv.lock /code/uv.lock
COPY ./pyproject.toml /code/pyproject.toml

RUN pip install uv

RUN uv sync

COPY ./app /code/app

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]
