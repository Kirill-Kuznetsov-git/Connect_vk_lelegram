FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ../../project/vk_bot/vk_bot.py .
COPY ../../project/api_messages .
COPY docker_files/vk_bot/requirements.txt .
RUN pip install -r requirements.txt
CMD ['python', 'vk_bot.py']