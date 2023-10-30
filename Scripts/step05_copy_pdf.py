# -*- coding: utf-8 -*-

class step05_copy_pdf():
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

        filepath_01 = os.path.join(knowledge_dir, "COPY.md")
        with open(filepath_01, "a") as f01:
            f01.write("# section-2\n")
            with open(os.path.join(prev_knowledge_dir, "pdf_database.txt"), "r") as f:
                for line in f.readlines():
                    f01.write(line.replace("^#### ", "##### ").replace("^### ", "#### ").replace("^## ", "### ").replace("^# ", "## "))

        print(msg, " ... OK")

if __name__ == '__main__':
    step05_copy_pdf().run("")
