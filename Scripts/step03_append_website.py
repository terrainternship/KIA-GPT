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

        def append_with_conflicts_using_neuro_copyrighter(dir):
            return False

        def append_as_is(knowledge_dir):
            filepath_00 = os.path.join(knowledge_dir, "TRASH.md")
            with open(filepath_00, "a") as f00:
                with open("example.txt", "r") as fe:
                    with open(os.path.join(knowledge_dir, "__parser_database.txt"), "r") as fr:
                        pass
            return True

        if not append_with_conflicts_using_neuro_copyrighter(dir):
            append_as_is(dir)

        print(msg, " ... OK")

if __name__ == '__main__':
    step03_append_website().run("")
