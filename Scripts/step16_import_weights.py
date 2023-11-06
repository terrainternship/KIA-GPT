# -*- coding: utf-8 -*-

class step16_import_weights():
    def __init__(self):
        pass

    def run(self, msg):
        import configparser
        import pathlib
        import os
        config = configparser.ConfigParser()
        config.read('config.txt')
        knowledge_dir = config["COLAB"]["knowledge_dir"]
        if knowledge_dir is None: knowledge_dir = "./knowledge"
        pathlib.Path(knowledge_dir).mkdir(parents=True, exist_ok=True)
        prev_knowledge_dir = config["COLAB"]["prev_knowledge_dir"]
        if prev_knowledge_dir is None: prev_knowledge_dir = "../knowledge"
        pathlib.Path(prev_knowledge_dir).mkdir(parents=True, exist_ok=True)

        import getpass
        import openai

        if config["CHATGPT"]["api_key"] == "?":
            openai_key = getpass.getpass("OpenAI API Key:")
        else:
            openai_key = config["CHATGPT"]["api_key"]
        os.environ["OPENAI_API_KEY"] = openai_key
        openai.api_key = openai_key

        from langchain.text_splitter import MarkdownHeaderTextSplitter
        import re
        from langchain.vectorstores import FAISS

        def save_file_knowledge(file_path: str, out_path: str) -> str:
            # Чтение текстового файла
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()

            headers_to_split_on = [
                ("#", "Header 1"),
                ("##", "Header 2"),
                ("###", "Header 3"),
                ("####", "Header 4"),
            ]

            markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
            md_header_splits = markdown_splitter.split_text(text)

            # Предполагается, что FAISS и OpenAIEmbeddings были импортированы или определены где-то выше
            vectordateBase = FAISS.from_documents(md_header_splits, OpenAIEmbeddings())
            vectordateBase.save_local(out_path)

            return out_path

        save_file_knowledge(os.path.join(knowledge_dir, "info.md"), os.path.join(knowledge_dir, "info_faiss"))
        save_file_knowledge(os.path.join(knowledge_dir, "howto.md"), os.path.join(knowledge_dir, "howto_faiss"))
        print(msg, " ... OK")

if __name__ == '__main__':
    step16_import_weights().run("")