
from gpt import OpenAIHandler
import os
import platform
os.environ['TERM'] = 'xterm'


OpenGPT = OpenAIHandler()



def clear_screen():
    system_platform = platform.system()  # определить операционную систему
    if system_platform == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def insert_newlines(textstr: str, max_len: int = 170) -> str:
    words = textstr.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line + " " + word) > max_len:
            lines.append(current_line)
            current_line = ""
        current_line += " " + word
    lines.append(current_line)
    return "\n".join(lines)


def run_dialog():
    while True:
        user_question = input('\nВопрос: ')
        if ((user_question.lower() == 'stop') or (user_question.lower() == 'стоп')):
            break
        answer = OpenGPT.answer_index(user_question)
        print('\nОтвет: ', insert_newlines(answer))

    return

clear_screen()
#START APP
run_dialog()