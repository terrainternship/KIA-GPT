# базовый образ
FROM python:3.9

# рабочая директория
WORKDIR /usr/src/TGbot

# копируем проект
COPY . /usr/src/TGbot

# установка библиотек
RUN pip install -r requirements.txt

# запуск бота
CMD ["python", "async_chatGPT.py"]