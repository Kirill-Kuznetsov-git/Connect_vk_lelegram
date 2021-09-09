FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ../../project/telegram_bot/telegram_bot.py .
COPY docker_files/telegram_bot/requirements.txt .
RUN pip install -r requirements.txt
CMD ['python', 'telegram_bot.py']