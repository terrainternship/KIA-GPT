# -*- coding: utf-8 -*-

class step03_append_website():
    def __init__(self):
        pass

    def run(self, msg):
        import configparser
        import pathlib
        config = configparser.ConfigParser()
        config.read('config.txt')
        knowledge_dir = config["DEFAULT"]["knowledge_dir"]
        if knowledge_dir is None: knowledge_dir = "./knowledge"
        pathlib.Path(knowledge_dir).mkdir(parents=True, exist_ok=True)

        def append_with_conflicts_using_neuro_copyrighter():
            return False

        def append_as_is():
            import langchain
            import re
            return True

        if not append_with_conflicts_using_neuro_copyrighter():
            append_as_is()

        print(msg, " ... OK")

if __name__ == '__main__':
    step03_append_website().run("")
