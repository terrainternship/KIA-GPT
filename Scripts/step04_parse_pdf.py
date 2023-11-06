# -*- coding: utf-8 -*-

class step04_parse_pdf():
    def __init__(self):
        pass

    def run(self, msg):
        import configparser
        import pathlib
        import shutil
        import os
        config = configparser.ConfigParser()
        config.read('config.txt')
        knowledge_dir = config["COLAB"]["knowledge_dir"]
        if knowledge_dir is None: knowledge_dir = "./knowledge"
        pathlib.Path(knowledge_dir).mkdir(parents=True, exist_ok=True)
        prev_knowledge_dir = config["COLAB"]["prev_knowledge_dir"]
        if prev_knowledge_dir is None: prev_knowledge_dir = "../knowledge"
        pathlib.Path(prev_knowledge_dir).mkdir(parents=True, exist_ok=True)
        shutil.copyfile(os.path.join(prev_knowledge_dir, "pdf_database.txt"), os.path.join(knowledge_dir, "pdf_database.txt"))
        """
        # импортируем нужные библиотеки
        import requests
        from bs4 import BeautifulSoup
        import re
        import numpy as np
        import os
        from tika import parser



        # cкачиваем фалы данных в виде csv

        def load_document_csv(url: str) -> str:
            # Extract the document ID from the URL
            match_ = re.search('/spreadsheets/d/([a-zA-Z0-9-_]+)', url)
            if match_ is None:
                raise ValueError('Invalid Google Docs URL')
            doc_id = match_.group(1)

            # Download the document as plain text
            response = requests.get(f'https://docs.google.com/spreadsheets/d/{doc_id}/export?format=tsv')
            response.raise_for_status()
            text = response.content

            return text

        urls = load_document_csv('https://docs.google.com/spreadsheets/d/1h5BNBTXwzb8nMTIcre0vCDcujax1Fvfw3RdwT7FeAt8/edit?usp=sharing')
        with open('urls_r.csv','wb') as f:
          f.write(urls)

        # загружаем ссылки из файла данных в массим Numpy
        links = np.genfromtxt('urls_r.csv', delimiter='\t', dtype=str, encoding='utf-8' )


        '''
        Эта функция находит все файлы pdf на странице сайта.

        Вход:
          url - адрес страницы сайта
        Выход:
          title - заголовок страницы
          PDF_name - словарь в котором key - это название тега, value - ссылка на файл
        '''

        def find_pdf(url: str) -> str:

          # заводим переменную для названия страницы сайта
          title = ""
          # Заводим пустой словарь для списка pdf файлов
          PDF_name = {}

          # Получаем запрос от страницы
          response = requests.get(url)
          # Получаем ПрекрасныйСуп
          bs = BeautifulSoup(response.text, "html.parser")
          # сохраняем заголовок страницы
          title = bs.title.string

          # Определяем функцию отбора тегов. Берём теги у которых есть ссылка.
          def have_href(href):
            return href

          # Отбитаем теги у которых есть ссылка
          bs.find_all(href = have_href)


          # Наполняем словарь описаниями файла и ссылками
          # То, что это словарь - важно.
          # Так мы избегаем одинаковых файлов, но с разными ссылками. (такое есть)
          for tag in bs.find_all(href = have_href):
              # Извлекаем ссылку из тега
              tag_href = tag.attrs['href']
              # Делаем условие, если ссылка на файл, который оканчивается на .pdf
              if tag_href.split('.')[-1] == 'pdf' and \
                ("Обзор функций (PDF)" not in tag.get_text()): # это условие только для сайта KIA
                # Добавляем новый элемент в словарь
                PDF_name[tag.get_text().strip()] = tag_href
          # Возвращаем словарь
          return title, PDF_name

          # Смотрим, как работает функция на примере одной станицы сайта:

          '''
          Эта функция принимает на вход URL-адрес
          по которому находится pdf файл, переводит его в текстовый формат
          при помощи tika и сохраняет на диск.

            Вход:
              url - адрес PDF файла
            Выход:
              topic - текст
          '''

          def pdf_to_txt_tika(url):
            topic = ''
            # pattern = re.compile(r'\w[а-я]')
            # получаем файл
            pdf_req = requests.get(url)
            # проверяем, что ссылка удачно парсится
            if pdf_req.status_code == 200:
              # запоминаем название файла без расширения
              f_name = os.path.basename(url).split('.')[0]
              # записываем файл на диск
              with open(f'{f_name}.pdf','wb') as f:
                f.write(pdf_req.content)

              # парсим pdf файл
              reader = parser.from_file(f'{f_name}.pdf')
              # сохраняем текст в переменную
              text = reader['content']
              # убираем спецсимволы
              text = re.sub(u"\uFFFD",' ', text)
              # убираем повторяющиеся пробелы внутри строки
              text = re.sub('\u0020+',' ', text)
              # убираем ошибочные разрывы абзацев
              text = text.replace(' \n\n', '\n')
              text = text.replace('. \n', '\n')
              text = text.replace(': \n', ':\n')
              text = text.replace('; \n', ';\n')
              text = text.replace(' \n', ' ')
              text = text.replace('-\n', '-')
              # разбиваем текст на строки для дальнейшей обработки
              txt_split = text.split('\n')

              # начинаем исправлять типичные ошибки парсера
              for st in txt_split:
                # убираем пробелы в начале строки
                st = st.lstrip()
                # проверям, что строка это не номер страницы
                num = re.match("^[0-9\s*]+$", st)
                # если строка не пустая и не номер страницы - добавляем её к тексту
                if not num and st:
                  topic += st + '\n'

              topic = topic.replace(u' \u2022', u'\n\u2022')

              # снова разбиваем текст на строки для дальнейшей обработки
              txt_split = topic.split('\n')
              topic = ''

              for st in txt_split:
                if st:
                  if re.match('[а-яёa-zA-Z\u00AB]', st[0]) and st:
                    topic += ' ' + st
                  else:
                    topic += '\n' + st


              # и снова разбиваем текст, чтобы убрать повторы
              txt_split = topic.split('\n')
              topic = ''
              last_st = ''

              for st in txt_split:
                if last_st != st:
                  topic +=  st + '\n'
                last_st = st


              # стираем pdf файл
              if os.path.isfile(f'{f_name}.pdf'):
                os.remove(f'{f_name}.pdf')

              # записываем текст в файл с названием оригинала, но txt
              with open(f'{f_name}.txt','w') as f:
                f.write(topic)

              return topic

        """

        print(msg, " ... OK")


if __name__ == '__main__':
    step04_parse_pdf().run("")
