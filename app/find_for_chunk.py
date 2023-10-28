from langchain.llms import OpenAI
from langchain.docstore.document import Document
import requests
#database
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
import re
import getpass
import os
import openai




class OpenAIHandler:

    PROMT = ''
    url_promt='https://docs.google.com/document/d/1i8HA7cX4Ut-tb9rf8wOgERU7lLe66xJYscizGtSSJl0'

    MODEL_GPT_3_5_TURBO_16K = ['gpt-3.5-turbo-16k', 0.003, 0.004]
    MODEL_GPT_3_5_TURBO = ['gpt-3.5-turbo', 0.0015, 0.002]  # 4,097 tokens
    MODEL_GPT_3_5_TURBO_INSTRUCT = ['gpt-3.5-turbo-instruct', 0.0015, 0.002]  # 4,097 tokens
    MODEL_GPT_4 = ['gpt-4', 0.03, 0.06]  # 8,192 tokens
    SELECT_MODEL_GPT = MODEL_GPT_4




    def setOpenAI(self):
        # Это надо первести на .env
        openai_key = getpass.getpass("OpenAI API Key:") 
        os.environ["OPENAI_API_KEY"] = openai_key
        openai.api_key = openai_key


    # функция для загрузки документа по ссылке из гугл драйв
    def load_document_text(self, url: str) -> str:
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

    def load_knowledge(self):
        self.knowledge_only_langchain = FAISS.load_local('./knowledge/faiss', OpenAIEmbeddings())
   

    def load_promt(self):
        self.PROMT = self.load_document_text(self.url_promt)



    def answer_index(self, topic, temp=0.1, top_similar_documents=3):
            if self.PROMT == '': 
                print('1111111====================='+self.PROMT) 
                return 'Promt is clear'

           # os.system('cls||clear')
            docs = self.knowledge_only_langchain.similarity_search_with_score(topic, k=top_similar_documents)
        
            responses = []
            for i, (doc, score) in enumerate(docs):
                if score < 1: # ТУТ ТЫ МОЖЕШЬ УПРАВЛЯТЬ праметром Л2 для чанков. 0..1
                    content = doc.page_content
                    response = f'\n=====================Отрывок документа №{i + 1}=====================\n{content}\n'
                    print(f'\n=====================Отрывок документа №{i + 1}=====================\n')
                    print(f'=== score = {score}  Metadata документа ------------ {doc.metadata}')
                    print(f' \n{content}\n')
                    responses.append(response)
            return  ' '
