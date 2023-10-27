# Необходимо установить нужные библиотеки описано в РИДМИ
from langchain.llms import OpenAI
from langchain.docstore.document import Document
import requests
#database
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
import pathlib
import subprocess
import tempfile
import re
import getpass
import os
import platform
import openai
#import tiktoken
from langchain.text_splitter import MarkdownHeaderTextSplitter
import re
from langchain.chains.router import MultiPromptChain
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate

PROMT=''
url_promt='https://docs.google.com/document/d/1i8HA7cX4Ut-tb9rf8wOgERU7lLe66xJYscizGtSSJl0'

MODEL_GPT_3_5_TURBO_16K = ['gpt-3.5-turbo-16k', 0.003, 0.004]
MODEL_GPT_3_5_TURBO = ['gpt-3.5-turbo', 0.0015, 0.002]  # 4,097 tokens
MODEL_GPT_3_5_TURBO_INSTRUCT = ['gpt-3.5-turbo-instruct', 0.0015, 0.002]  # 4,097 tokens
MODEL_GPT_4 = ['gpt-4', 0.03, 0.06]  # 8,192 tokens
SELECT_MODEL_GPT = MODEL_GPT_4


models_template = """You are a very smart assistant for Kia. You know everything about KIA car models
You are excellent at answering questions about Kia car models concisely and clearly.
When you don't know the answer to a question, you admit that you don't know.

Here is a question:
{input}"""

technology_template = """You are a very smart assistant for KIA. You know everything about the technologies used in KIA cars.
You are excellent at answering questions briefly and clearly about the technologies used in KIA cars.
When you don't know the answer to a question, you admit that you don't know.

Here is a question:
{input}"""

parts_template = """You are a very smart assistant for KIA. You know all the information on spare parts for KIA cars.
You are excellent at answering questions about spare parts for KIA cars briefly and clearly.
When you don't know the answer to a question, you admit that you don't know.

Here is a question:
{input}"""

oils_template = """You are a very smart assistant for KIA. You know all the information on engine oils for KIA cars.
You are excellent at answering questions about engine oils for KIA cars briefly and clearly.
When you don't know the answer to a question, you admit that you don't know.

Here is a question:
{input}"""

tech_template = """You are a very smart assistant for KIA. You know everything about the maintenance of KIA cars.
You are excellent at answering questions about KIA vehicle maintenance briefly and clearly.
When you don't know the answer to a question, you admit that you don't know.

Here is a question:
{input}"""

accessories_template = """You are a very smart assistant for KIA. You know all the information about accessories for KIA cars.
You are excellent at answering questions about accessories for KIA cars concisely and clearly.
When you don't know the answer to a question, you admit that you don't know.

Here is a question:
{input}"""

warranty_template = """You are a very smart assistant for KIA. You know all the information about the warranty for KIA cars.
You are excellent at answering questions about KIA vehicle warranties concisely and clearly.
When you don't know the answer to a question, you admit that you don't know.

Here is a question:
{input}"""

service_template = """You are a very smart assistant for KIA. You know all the information about servicing KIA cars.
You are excellent at answering questions about service for KIA vehicles briefly and clearly.
When you don't know the answer to a question, you admit that you don't know.

Here is a question:
{input}"""

sales_template = """You are a very smart assistant for KIA. You know all the information about KIA car sales.
You are excellent at answering questions about KIA car sales briefly and clearly.
When you don't know the answer to a question, you admit that you don't know.

Here is a question:
{input}"""

apps_template = """You are a very smart assistant for KIA. You know all the information about KIA software.
You are excellent at answering questions about KIA software briefly and clearly.
When you don't know the answer to a question, you admit that you don't know.

Here is a question:
{input}"""

promotion_template = """You are a very smart assistant for KIA. You know everything about promotions of KIA company.
You are excellent at answering questions about promotions of KIA company concisely and clearly.
When you don't know the answer to a question, you admit that you don't know.

Here is a question:
{input}"""


def setOpenAI():
    # Это надо первести на .env
    openai_key = getpass.getpass("OpenAI API Key:") 
    os.environ["OPENAI_API_KEY"] = openai_key
    openai.api_key = openai_key


# функция для загрузки документа по ссылке из гугл драйв
def load_document_text(url: str) -> str:
    # Extract the document ID from the URL
    match_ = re.search('/document/d/([a-zA-Z0-9-_]+)', url)
    if match_ is None:
        raise ValueError('Invalid Google Docs URL')
    doc_id = match_.group(1)

    # Download the document as plain text
    response = requests.get(f'https://docs.google.com/document/d/{doc_id}/export?format=txt')
    response.raise_for_status()
    text = response.text
    return text


# def load_file_knowledge(file_path: str) -> str:
#     # Чтение текстового файла
#     with open(file_path, 'r', encoding='utf-8') as file:
#         text = file.read()

#     headers_to_split_on = [
#         ("#", "router"),
#         ("##", "Header2"),
#         ("###", "Header3"),
#         ("####", "Header4"),
#     ]

#     markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
#     md_header_splits = markdown_splitter.split_text(text)

#     # Предполагается, что FAISS и OpenAIEmbeddings были импортированы или определены где-то выше
#     vectordateBase = FAISS.from_documents(md_header_splits, OpenAIEmbeddings())

#     return vectordateBase

def init_routing():
    



def load_knowledge():
    models_knowledge_base = load_file_knowledge('models.md')
    technology_knowledge_base = load_file_knowledge('technology.md')
    parts_knowledge_base = load_file_knowledge('parts.md')
    oils_knowledge_base = load_file_knowledge('oils.md')
    tech_knowledge_base = load_file_knowledge('tech.md')
    accessories_knowledge_base = load_file_knowledge('accessories.md')
    warranty_knowledge_base = load_file_knowledge('warranty.md')
    service_knowledge_base = load_file_knowledge('service.md')
    sales_knowledge_base = load_file_knowledge('sales.md')
    apps_knowledge_base = load_file_knowledge('apps.md')
    promotions_knowledge_base = load_file_knowledge('promotions.md')
    #none_knowledge_base = load_file_knowledge('none.md')

def load_promt():
     PROMT = load_document_text (url_promt)


def answer_index(topic, temp=0.1, top_similar_documents=3):

        if PROMT == '': 
            print('Promt is clear') 
            return 'Promt is clear'

        router_result = router_chain.__call__({"input": topic})
        chosen_route = router_result['destination']
        next_inputs = router_result['next_inputs']
        print(f"Выбранный маршрут: {chosen_route}")
        print(f"Следующие входные данные: {next_inputs}")

        unit_to_multiplier = {
            'models':  models_knowledge_base,
            'technology': technology_knowledge_base,
            'parts':  parts_knowledge_base,
            'oils': oils_knowledge_base,
            'tech': tech_knowledge_base,
            'accessories': accessories_knowledge_base,
            'warranty': warranty_knowledge_base,
            'service': service_knowledge_base,
            'sales': sales_knowledge_base,
            'apps': apps_knowledge_base,
            'promotions': promotions_knowledge_base
        }

        knowledge_base = unit_to_multiplier.get(chosen_route, None)
        if knowledge_base is not None:
            docs = knowledge_base.similarity_search_with_score(topic, k=top_similar_documents)
        else:
            return  'Вопрос не понятен!!!'


        responses = []
        for i, (doc, score) in enumerate(docs):
            if score < 1: # ТУТ ТЫ МОЖЕШЬ УПРАВЛЯТЬ праметром Л2 для чанков. 0..1
                content = doc.page_content
                response = f'\n=======Отрывок документа №{i + 1}=====\n{content}\n'
                print(f'\n=====================Отрывок документа №{i + 1}=====================\n')
                print(f'=== score = {score}  Metadata документа ------------ {doc.metadata}')
                print(f'\n{content}\n')
                responses.append(response)


        messages = [
            {"role": "system", "content": PROMT},
            {"role": "user",
             "content": f"Документ с информацией для ответа клиенту: {responses}\n\nВопрос клиента: \n{topic}"}
        ]

        completion = openai.ChatCompletion.create(
            model=SELECT_MODEL_GPT[0],
            messages=messages,
            temperature=temp
        )

        answer = completion.choices[0].message.content

        return  answer
