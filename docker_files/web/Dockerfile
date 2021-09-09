FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY docker_files/web/requirements.txt .
RUN pip install -r requirements.txt
COPY . .
