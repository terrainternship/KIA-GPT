# -*- coding: utf-8 -*-

class step03_append_website():
    def __init__(self):
        pass

    def run(self, msg):
        import configparser
        import pathlib
        import os
        config = configparser.ConfigParser()
        config.read('config.txt')
        knowledge_dir = config["DEFAULT"]["knowledge_dir"]
        if knowledge_dir is None: knowledge_dir = "./knowledge"
        pathlib.Path(knowledge_dir).mkdir(parents=True, exist_ok=True)
        filepath_01 = os.path.join(knowledge_dir, "__parser_database.txt")
        with open(filepath_01, "w") as f01:
            f01.write("")
        print(msg, " ... OK")

if __name__ == '__main__':
    step03_append_website().run("")
