import os
from dotenv import load_dotenv

load_dotenv()

def get_TEMPERATURE():
    try:
        value = os.environ['TEMPERATURE']
    except KeyError:
        print("\033[91m Ошибка: \033[92m переменная окружения TEMPERATURE не установлена! \033[0m")
        # Здесь вы можете предпринять дополнительные действия, например, завершить выполнение программы
        exit(1)
    return value


def get_SECRET_OPENAI_KEY():
    try:
        value = os.environ['SECRET_OPENAI_KEY']
    except KeyError:
        print("\033[91m Ошибка: \033[92m переменная окружения SECRET_OPENAI_KEY не установлена! \033[0m")
        # Здесь вы можете предпринять дополнительные действия, например, завершить выполнение программы
        exit(1)
    return value

def get_PROMPT_URL():
    try:
        value = os.environ['PROMPT_URL']
    except KeyError:
        print("\033[91m Ошибка: \033[92m переменная окружения PROMPT_URL не установлена! \033[0m")
        # Здесь вы можете предпринять дополнительные действия, например, завершить выполнение программы
        exit(1)
    return value

def get_KNOWLEDGE_URL():
    try:
        value = os.environ['KNOWLEDGE_URL']
    except KeyError:
        print("\033[91m Ошибка: \033[92m переменная окружения KNOWLEDGE_URL не установлена! \033[0m")
        # Здесь вы можете предпринять дополнительные действия, например, завершить выполнение программы
        exit(1)
    return value

# def SUMMARIZE_ON():
#     '''Функция берет значение саммаризации из энв файла'''
#     try:
#         value = os.environ['SUMMARIZE_ON']
#     except KeyError:
#         print("\033[91m Ошибка: \033[92m переменная окружения SUMMARIZE_ON не установлена! \033[0m")
#         # Здесь вы можете предпринять дополнительные действия, например, завершить выполнение программы
#         exit(1)
#     return value

def SUMMARIZE_ON():
    # Функция берет значение саммаризации из .env файла
    value = os.getenv('SUMMARIZE_ON')
    if value == "True":
        return True
    elif value == "False":
        return False
    else:
        print("\033[91m Ошибка: \033[92m переменная окружения SUMMARIZE_ON должна быть True or False! \033[0m")
        # Здесь вы можете предпринять дополнительные действия, например, завершить выполнение программы
        exit(1)