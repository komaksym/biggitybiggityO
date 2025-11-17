FROM nvidia/cuda:13.0.2-runtime-ubuntu24.04

WORKDIR /code

RUN apt-get update --fix-missing \
    && apt-get install -y --no-install-recommends \ 
        python3 python3-pip python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Set PATH to use venv Python by default
ENV PATH="/opt/venv/bin:$PATH"

# Ensure pip in venv is upgraded
RUN pip install --upgrade pip

# Then install requirements in the venv
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt


COPY ./app /code/app

EXPOSE 8000

CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]
