# -*- coding: utf-8 -*-

class step07_copy_video():
    def __init__(self):
        pass

    def run(self, msg):
        import tiktoken

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

        def num_tokens_from_messages(model, messages):
            """Returns the number of tokens used by a list of messages."""
            try:
                encoding = tiktoken.encoding_for_model(self.model)
            except KeyError:
                encoding = tiktoken.get_encoding("cl100k_base")
            if model in ["gpt-3.5-turbo-0613", "gpt-3.5-turbo-16k", "gpt-4-0613"]:  # note: future models may deviate from this
                num_tokens = 0
                for message in messages:
                    num_tokens += 4  # every message follows {role/name}\n{content}\n
                    for key, value in message.items():
                        num_tokens += len(encoding.encode(value))
                        if key == "name":  # if there's a name, the role is omitted
                            num_tokens += -1  # role is always required and always 1 token
                num_tokens += 2  # every reply is primed with assistant
                return num_tokens
            else:
                raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.  See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")

        info_cnt = 0
        while True:
            last_md_level_01 = "#"
            last_md_level_02 = "##"
            last_md_level_03 = "###"
            with open(os.path.join(prev_knowledge_dir, "pdf_database.txt"), "r") as f:
                info_cnt = info_cnt + 1
                filepath_01 = os.path.join(knowledge_dir, f"INFO-{info_cnt}.md")
                with open(filepath_01, "w") as f01:
                    # f01.write("# info\n")
                    for line in f.readlines():
                        f01.write(line.replace("^#### ", "##### ").replace("^### ", "#### ").replace("^## ", "### ").replace("^# ", "## "))
            break

        howto_cnt = 0
        while True:
            last_md_level_01 = "#"
            last_md_level_02 = "##"
            last_md_level_03 = "###"
            with open(os.path.join(prev_knowledge_dir, "video_database.txt"), "r") as f:
                howto_cnt = howto_cnt + 1
                filepath_02 = os.path.join(knowledge_dir, f"HOWTO-{howto_cnt}.md")
                with open(filepath_02, "w") as f02:
                    # f02.write("# howto\n")
                    for line in f.readlines():
                        f02.write(line.replace("^#### ", "##### ").replace("^### ", "#### ").replace("^## ", "### ").replace("^# ", "## "))
            break

        print(msg, " ... OK")

if __name__ == '__main__':
    step07_copy_video().run("")
