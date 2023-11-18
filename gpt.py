
import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import MarkdownHeaderTextSplitter
import openai
import config
import shutil


class OpenAIHandler:
    MODEL_GPT_3_5_TURBO = ['gpt-3.5-turbo', 0.001, 0.002]  # 4,097 tokens
    MODEL_GPT_3_5_TURBO_16K = ['gpt-3.5-turbo-16k', 0.003, 0.004]
    MODEL_GPT_3_5_TURBO_INSTRUCT_4K = ['gpt-3.5-turbo-instruct', 0.0015, 0.002]
    MODEL_GPT_4 = ['gpt-4', 0.03, 0.06]  # 8,192 tokens
    MODEL_GPT_4_32K = ['gpt-4-32k', 0.06, 0.12]
    MODEL_GPT_4_PREVIEW = ['gpt-4-1106-preview', 0.01, 0.03]  
    MODEL_GPT_4_VISIO = ['gpt-4-1106-preview', 0.01, 0.03]  
    SELECT_MODEL_GPT = MODEL_GPT_3_5_TURBO_16K

    HISTORY = []
    summDialog = ''


    def __init__(self, summarize_flag=False):
        print('\n\n\033[93m=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Подготовка к запуску=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=\n\033[0m')
        openai_key = config.get_SECRET_OPENAI_KEY()
        os.environ["OPENAI_API_KEY"] = openai_key
        openai.api_key = openai_key

        self._load_prompt_from_file()
        self._load_knowledge_from_file()

        print('\n\n\033[93m=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-Этап подготовки завершен! Запуск программы! Задайте вопрос. =-=-=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=\n\033[0m')



    def _load_prompt_from_file(self):
        try:
            with open(f'{config.get_PROMPT_URL()}', 'r') as prompt_file:
                self.prompt = prompt_file.read()
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            exit(1)


    # Функция для запроса подтверждения от пользователя
    def _confirm_replacement(self):
        directory_path = "vector_db"
        # Запрос ввода от пользователя
        if not os.path.exists(directory_path):
            # каталога с векторной базой нет! Нужно создавать новый
            return True
        else:
            # Проверка ответа пользователя
            print(f"Каталог {directory_path} уже существует.")
            user_input = input(
                "Заменить существующий каталог Базы знаний? \n (введите да/нет): ").lower().strip()
            if user_input == 'да' or user_input == '1':
                # Пользователь подтвердил замену файла
                shutil.rmtree(directory_path)
                print(f"Каталог {directory_path} удален.")
                return True
            else:
                # Пользователь не подтвердил замену файла
                return False


    def _load_knowledge_from_file(self):
        # load database
        directory_path = "vector_db"
        if self._confirm_replacement():
            print(f"Запущен процесс формирования новой векторной базы {directory_path} ")
            try:
                with open(f'{config.get_KNOWLEDGE_URL()}', 'r') as knowledge_file:
                    text = knowledge_file.read()
            except Exception as e:
                print(f"Произошла ошибка: {e}")
                exit(1)

            headers_to_split_on = [
                ("#", "router"),
                ("##", "theme"),
                ("###", "Header3"),
                ("####", "Header4"),
            ]

            markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
            md_header_splits = markdown_splitter.split_text(text)
            self.knowledge_base = FAISS.from_documents(md_header_splits, OpenAIEmbeddings())
            self.knowledge_base.save_local(directory_path)
            print(f"Каталог {directory_path} создан.")
        else:
            self.knowledge_base = FAISS.load_local(directory_path, OpenAIEmbeddings())

    def _summarize_topic(self, dialog):
        messages = [
            {"role": "system",
             "content": "Ты - ассистент консультанта, основанный на AI. Ты умеешь профессионально суммаризировать присланные тебе диалоги консультанта и клиента. Твоя задача - суммаризировать диалог, который тебе пришел. Обязательно выбери Имя клиента. Выбери ключевые слова таким образом, чтобы диалог должен быть не более 50 слов"},
            {"role": "user",
             "content": "Суммаризируй следующий диалог консультанта и клиента: " + " ".join(dialog)}
        ]

        completion = openai.ChatCompletion.create(
            model=self.SELECT_MODEL_GPT[0],
            messages=messages,
            temperature=0.1,  # Используем более низкую температуру для более определенной суммаризации
            max_tokens=3000  # Ограничиваем количество токенов для суммаризации
        )
        return completion.choices[0].message.content
    
    def answer_index(self, topic, temp=float(f'{config.get_TEMPERATURE()}'), top_similar_documents=10):
      #  print('\n\n\033[93m=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Новый вопрос=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=\n\033[0m')
        # Добавляем явное разделение между историей диалога и текущим вопросом
        if not summarize_flag:
            self.HISTORY = '' # ОТКЛЮЧАЕТ САММАРИЗАЦИЮ! ЕСТЬ НУЖНО ЕЕ ВКЛЮЧИТЬ ТОГДА ЗАКОММЕНТИРУЙ
        if len(self.HISTORY) > 0:
            self.summDialog = self._summarize_topic(
                ["Вот краткий обзор предыдущего диалога: " + summ +
                 '\nВопрос клиента: ' + ques + (('. Ответ консультанта: ' + ans)
                  if ans is not None else '') for summ, ques, ans in self.HISTORY])
            #print(f'САММАРИ \n=== {insert_newlines(self.summDialog)} \n')

        # Добавляем явное разделение между историей диалога и текущим вопросом
        input_text = "Вот краткий обзор предыдущего диалога: " + self.summDialog + "\nТекущий вопрос: " + topic

        #docs = self.knowledge_base.similarity_search(topic, k=top_similar_documents)
        # message_content = re.sub(r'\n{2}', ' ', '\n '.join(
        #     [f'\nОтрывок документа №{i + 1}\n=====================' + doc.page_content + '\n' for i, doc in
        #      enumerate(docs)]))

       # print(f'Вопрос пользователя \n=== {topic} \n')

        docs = self.knowledge_base.similarity_search_with_score(input_text, k=top_similar_documents)
        responses = []
        for i, (doc, score) in enumerate(docs):
            if score < 2:
                content = doc.page_content
                response = f'\n====Отрывок документа №{i + 1}=====\n{content}\n'
              #  print(f'\n=====================Отрывок документа №{i + 1}=====================\n')
              #  print(f'=== score = {score}  Metadata документа ------------ {doc.metadata}')
              #  print(f' \n{content}\n')
                responses.append(response)

        messages = [
            {"role": "system", "content": self.prompt},
            {"role": "user",
                "content": f"Документ с информацией для ответа пользователю: {responses}\n\nВопрос клиента: \n{input_text}"}
        ]

        completion = openai.ChatCompletion.create(
            model=self.SELECT_MODEL_GPT[0],
            messages=messages,
            temperature=temp
        )

        answer = completion.choices[0].message.content

        # Добавляем вопрос пользователя и ответ системы в историю
        self.HISTORY = []
        self.HISTORY.append((self.summDialog, topic, answer if answer is not None else ''))

        return answer  # возвращает ответ
