# Необходимо установить нужные библиотеки описано в РИДМИ
from langchain.llms import OpenAI
from langchain.docstore.document import Document
import requests
#database
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
#from langchain.document_loaders import TextLoader
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

PROMT=''

MODEL_GPT_3_5_TURBO_16K = ['gpt-3.5-turbo-16k', 0.003, 0.004]
MODEL_GPT_3_5_TURBO = ['gpt-3.5-turbo', 0.0015, 0.002]  # 4,097 tokens
MODEL_GPT_3_5_TURBO_INSTRUCT = ['gpt-3.5-turbo-instruct', 0.0015, 0.002]  # 4,097 tokens
MODEL_GPT_4 = ['gpt-4', 0.03, 0.06]  # 8,192 tokens
SELECT_MODEL_GPT = MODEL_GPT_4


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



def load_promt():
     PROMT = load_document_text ('https://docs.google.com/document/d/1i8HA7cX4Ut-tb9rf8wOgERU7lLe66xJYscizGtSSJl0')


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
            {"role": "system", "content": prompt},
            {"role": "user",
             "content": f"Документ с информацией для ответа клиенту: {responses}\n\nВопрос клиента: \n{topic}"}
        ]

        completion = openai.ChatCompletion.create(
            model=SELECT_MODEL_GPT[0],
            messages=messages,
            temperature=temp
        )

        answer = completion.choices[0].message.content

        return  insert_newlines(answer)
