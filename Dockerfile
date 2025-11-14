FROM nvidia/cuda:12.1.1-runtime-ubuntu22.04

WORKDIR /code

RUN apt-get clean && rm -rf /var/lib/apt/lists/* \
    && apt-get update --fix-missing \
    && apt-get install -y --no-install-recommends \ 
        python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*
RUN python3 -m pip install --upgrade pip
RUN ln -s /usr/bin/python3 /usr/bin/python

COPY ./requirements.txt /code/requirements.txt 

RUN pip install -r requirements.txt

COPY ./app /code/app

EXPOSE 8000

CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]
