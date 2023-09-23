ARG BASE_IMAGE=python:3.9-slim-buster
FROM $BASE_IMAGE

ENV PYTHONUNBUFFERED 1

COPY . .
WORKDIR .

# pip & requirements
RUN python3 -m pip install --user --upgrade pip && \
    python3 -m pip install -r requirements.txt


# Execute
CMD ["python", "app.py"]
