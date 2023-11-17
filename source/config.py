import os
from dotenv import load_dotenv

load_dotenv()

def get_TGBOT_TOKEN():
    try:
        value = os.environ['TGBOT_TOKEN']
    except KeyError:
        print("Ошибка: переменная окружения TGBOT_TOKEN не установлена!")
        # Здесь вы можете предпринять дополнительные действия, например, завершить выполнение программы
        exit(1)
    return value