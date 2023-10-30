# -*- coding: utf-8 -*-

class step06_parse_video():
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
        shutil.copyfile(os.path.join(prev_knowledge_dir, "video_database.txt"),
                        os.path.join(knowledge_dir, "video_database.txt"))
        """
        import requests, json

        headers = {'referer': 'https://www.kia.ru/'}
        response = requests.get('https://www.kia.ru/ajax/video_bank/?limit=-1', headers=headers)

        jsonObj = json.loads(response.text)

        lists = jsonObj['content']['video_bank']['list']
        groups = jsonObj['content']['video_bank']['groups']

        urls = {}
        for list in lists:
            for video in lists[list]:
                urls[video['video_link']] = video['name']

        links = [i for i in urls.keys()]

        print(links)



        # Whisper.

        # model_size = "large-v2"
        # language = "russian"

        # Включите поддержку GPU
        # Зависимости, импорты и настройка

        # !pip install -qq git+https://github.com/openai/whisper.git
        # !pip install -qq langchain
        # !pip install -qq openai
        # !pip install -qq google-search-results

        # !pip install -qq python-docx
        # !pip install -U pytube
        # !pip install -qq tiktoken
        import whisper
        try:
          modelWhisper = whisper.load_model("large-v2")
          print("Загружена модель Whisper large-v2")
        except:
          print("ОШИБКА загрузки Whisper.")



        import os



        from psutil import virtual_memory
        ram_gb = virtual_memory().total / 1e9
        print('Your runtime has {:.1f} gigabytes of available RAM\n'.format(ram_gb))

        if ram_gb < 20:
          print('Not using a high-RAM runtime')
        else:
          print('You are using a high-RAM runtime!')

          #@title Импорт библиотек
        import os
        import re
        from pathlib import Path
        import json
        import ipywidgets as widgets
        from IPython.display import display
        from pytube import YouTube
        from tqdm.auto import tqdm
        import getpass
        import pickle

        import torch
        import tiktoken
        import whisper
        import openai

        from docx import Document
        from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

        # Сохраняем во временное хранилище
        import codecs

        ### @title  Импорты  OpenAI LLM
        from langchain.chains import ConversationChain         # Импортируем класс для создания цепочек диалогов
        from langchain.chat_models import ChatOpenAI           # Импортируем класс для работы с чатами на базе OpenAI
        from langchain.llms import OpenAI
        from langchain.memory import ConversationBufferMemory  # Импортируем класс для управления памятью диалогов
        from langchain.prompts import (
            ChatPromptTemplate,
            MessagesPlaceholder,
            SystemMessagePromptTemplate,
            HumanMessagePromptTemplate,
            PromptTemplate
        )
        from langchain.schema import (
            AIMessage,
            HumanMessage,
            SystemMessage
        )

        class WorkerWhisperОpenAI():
          def __init__(self, video_path = None, \
               Name = "Видео1", \
               NameLessons = "Имя Урока", \
               modelWhisper  = None, \
               whisper_file = None, \
               result_json_file = None, \
               chunks_pickle_file = None, \
               SAVE_DIR = '/content/drive/MyDrive/Colab Notebooks/ChatGPT/Video/TXT/', \
               modelОpenAI = 'gpt-3.5-turbo-0613'):   # 0301

            self.modelОpenAI = modelОpenAI
            self.YouTube_video_title = Name
            self.NameLessons = NameLessons
            self.SAVE_DIR = SAVE_DIR
            self.modelWhisper = modelWhisper

            # self.get_key_ОpenAI()
            self.encoding = tiktoken.encoding_for_model(self.modelОpenAI)
            self.titles_model = ChatOpenAI(temperature=0.1, max_tokens=300)
            self.summarization_model = ChatOpenAI(temperature=0.1, max_tokens=1000)

            self.video_path = video_path

            # загружаем сохраненный
            if whisper_file:
                with open(whisper_file, 'rb') as pick:
                  self.whisper_result = pickle.load(pick)

            # загружаем сохраненный .json
            if result_json_file:
                with open(result_json_file, "r") as f:
                    self.whisper_result = json.load(f)

            # загружаем сохраненный .pickle
            if chunks_pickle_file:
                with open(chunks_pickle_file, 'rb') as pick:
                  self.chunks = pickle.load(pick)


          # Транскрибация
          def get_whisper_result(self, ):

              # RTX3090: 21 минут обработка видео длинной 2 часа 45 минут на модели large-v2
              # Google Colab Tesla T4: 4 минут 52 секунды на обработку видео длинной 23 минуты 11 секунд на модели large-v2
              self.whisper_result = self.modelWhisper.transcribe(str(self.video_path), fp16=True, language="russian")

              with open(f'{self.SAVE_DIR}{self.YouTube_video_title}_whisper.json', "w") as f:
                f.write(str(self.whisper_result))

              # with open(f'{self.SAVE_DIR}{self.YouTube_video_title}_whisper.pickle', 'wb') as pick:
              #     pickle.dump(self.whisper_result, pick, protocol=pickle.HIGHEST_PROTOCOL)
              print('Файл whisper сохранен.')

        ### ---------------------------------------------------
        #### Группируем сегменты по токенам, чтобы в сегменте было не более 3000 токенов
          def grouping_segments_by_tokens(self):

              ## @title Группируем сегменты по предложениям
              def merge_chunks_by_sentences(chunks):
                  merged_chunks = []
                  current_chunk = None
                  for chunk in chunks:
                      if not current_chunk:
                          current_chunk = {"text": chunk["text"]}
                      elif current_chunk["text"][-1] in ['.', '!', '?']:
                          merged_chunks.append(current_chunk)
                          current_chunk = {"text": chunk["text"]}
                      else:
                          current_chunk["text"] += " " + chunk["text"]
                  if current_chunk:
                      merged_chunks.append(current_chunk)
                  return merged_chunks

              sentences = merge_chunks_by_sentences(self.whisper_result["segments"])
              for sentence in sentences:
                  if sentence["text"][-1] != ".":
                    sentence["text"] += "."

              # with open(f'{self.SAVE_DIR}{self.YouTube_video_title}_collecting.pickle', 'wb') as pick:
              #     pickle.dump(sentences, pick, protocol=pickle.HIGHEST_PROTOCOL)

              print(f"Ранее было предложений: {len(self.whisper_result['segments'])}")
              print(f"Стало предложений: {len(sentences)}")
              print("Группируем сегменты по токенам.")

              #@title Группируем сегменты по токенам(не более 3000)
              def merge_chunks_by_tokens(chunks, max_tokens=3000):
                  merged_chunks = []
                  current_chunk = None
                  for chunk_i, chunk in enumerate(chunks):
                      chunk_tokens_count = len(self.encoding.encode(chunk["text"]))
                      if not current_chunk:
                          current_chunk = {"text": chunk["text"], "tokens_count": chunk_tokens_count}
                      elif chunk_tokens_count + current_chunk["tokens_count"] > max_tokens:
                          merged_chunks.append(current_chunk)
                          assert current_chunk["tokens_count"] <= max_tokens + 1, current_chunk["tokens_count"]
                          current_chunk = {"text": chunk["text"], "tokens_count": chunk_tokens_count}
                      else:
                          current_chunk["text"] += " " + chunk["text"]
                          current_chunk["tokens_count"] = len(self.encoding.encode(current_chunk["text"]))

                  if current_chunk:
                      merged_chunks.append(current_chunk)
                  return merged_chunks

              try:
                self.chunks = merge_chunks_by_tokens(sentences)
                print(f"Было предложений: {len(sentences)}")
                print(f"Сгруппировали на  {len(self.chunks)}  блоков")
              except:
                self.chunks = merge_chunks_by_tokens(self.whisper_result["segments"])
                print(f"Альтернативный вариант. =========")
                print(f"Сгруппировали на  {len(self.chunks)}  блоков")

              # with open(f'{self.SAVE_DIR}{self.YouTube_video_title}_chunks.pickle', 'wb') as pick:
              #     pickle.dump(self.chunks, pick, protocol=pickle.HIGHEST_PROTOCOL)
              # print('Сгруппированные chunks - файл .pickle сохранен.')

              # # Создаем новый документ
              new_txt = ''
              for chunk_i, chunk in enumerate(self.chunks):
                  new_txt +=f"<Chunk>\n Урок:{self.NameLessons}\n"
                  new_txt +=chunk["text"] + "\n\n"

              with open(f'{self.SAVE_DIR}{self.YouTube_video_title}_grouping.txt', "w") as f:
                f.write(str(new_txt))
              print("Создали новый документ")


              # Транскрибация


              # https://youtu.be/twTVQ2F7Xnw
              YouTube_video_title = "Систематизация. 1 занятие"
              NameLessons = "Систематизация бизнеса. Занятие №1."
              SAVE_DIR = '/content/drive/MyDrive/_Projects_GPT/УИИ/'
              project_name = 'TXT_УИИ/'

              project_path = SAVE_DIR + project_name
              video_path = f'{SAVE_DIR}Video/{YouTube_video_title}.mp4'
              whisper_path = f'{SAVE_DIR}{project_name}{YouTube_video_title}_whisper.pickle'

              # Готовим класс для работы
              nature = WorkerWhisperОpenAI(video_path = video_path, \
                             Name = YouTube_video_title, \
                             NameLessons = NameLessons, \
                             modelWhisper = modelWhisper,\
                             SAVE_DIR = project_path)

              # nature = WorkerWhisperОpenAI(Name = YouTube_video_title, \
              #                              whisper_file = whisper_path)

              # nature = WorkerWhisperОpenAI(Name = YouTube_video_title, \
              #                              chunks_pickle_file = CHUNKS_pickle_file)
              ### ---------------------------------------------------
              # Собираем итоговую суммаризацию.
                def summarization(self):
                    print('Генерируем заголовки')
                    # Генерируем заголовки
                    for chunk in tqdm(self.chunks):
                        messages = [
                            SystemMessage(content='''
              Ты профессиональный копирайтер.
              Сделай короткий заголовок для фрагмента текста Лекции.
              Необходимо уложиться в 300 токенов.
              '''),
                            HumanMessage(content=chunk["text"])
                        ]
                        res = self.titles_model(messages)
                        chunk["title"] = res.content

                    print('Генерируем пересказ')
                    # Генерируем пересказ
                    for chunk in tqdm(self.chunks):
                        messages = [
                            SystemMessage(content='''
              Ты профессиональный копирайтер. У тебя большой опыт работы с Бизнесом в разных сферах, ты качественно структурируешь текст на Русском языке.

              Сделай формальный технический пересказ того, о чем рассказывает лектор на семинаре. Пиши от имени Лектора.
              Необходимо уложиться в 1000 токенов.
              '''),
              HumanMessage(content=chunk["text"])
                        ]
                        res = self.summarization_model(messages)
                        chunk["summarization"] = res.content

              # # Создаем новый документ
              new_txt = ''
              for chunk_i, chunk in enumerate(self.chunks):
                  new_txt +=f"<Chunk>\n Урок:{self.NameLessons}\n"
                  new_txt +=f"Тема: {chunk['title']}\n"
                  new_txt +=chunk["summarization"] + "\n\n"

              with open(f'{self.SAVE_DIR}{self.YouTube_video_title}_summ.txt', "w") as f:
                f.write(str(new_txt))
              print("Создали новый документ")

              # Транскрибация
              nature.get_whisper_result()

              # Группируем сегменты по токенам
              nature.grouping_segments_by_tokens()

              # Собираем итоговую суммаризацию.
              # Генерация субтитров и анализ текста
              nature.summarization()
        """

        print(msg, " ... OK")


if __name__ == '__main__':
    step06_parse_video().run("")
