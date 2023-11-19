
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


def run_dialog():
    while True:
        user_question = input('\nВопрос: ')
        if ((user_question.lower() == 'stop') or (user_question.lower() == 'стоп')):
            break
        answer = OpenGPT.answer_index(user_question)
        print('\nОтвет: ', OpenGPT.insert_newlines(answer)+'')

    return

clear_screen()
#START APP
run_dialog()