# -*- coding: utf-8 -*-

class step07_copy_video():
    def __init__(self):
        pass

    def run(self, msg):
        import pyaspeller
        import tiktoken
        import re
        import configparser
        import pathlib
        import os
        import time
        import random
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
                encoding = tiktoken.encoding_for_model(model)
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

        from pyaspeller import YandexSpeller
        speller = YandexSpeller()

        dict_databases = {"pdf_database.txt": "info", "video_database.txt": "howto"}
        for key in sorted(dict_databases.keys()):
            total_cnt = 0
            last_01_md_level_01 = None
            last_01_md_level_02 = None
            last_01_md_level_03 = None
            with open(os.path.join(prev_knowledge_dir, key), "r") as f:
                f01_lines = []
                for line in f.readlines():
                    line = speller.spelled(line)
                    time.sleep(random.randrange(1))
                    if len(line) > 253:
                        chunks, chunk_size = len(line)//253, 253
                        lines = [ line[i:i+chunk_size] for i in range(0, chunks, chunk_size)]
                        line = " ########## ".join(lines)
                    if re.match(("^#[^#]"), line) is not None:
                        last_01_md_level_01 = line
                        last_01_md_level_02 = None
                        last_01_md_level_03 = None
                    if re.match(("^##[^#]"), line) is not None:
                        last_01_md_level_02 = line
                        last_01_md_level_03 = None
                    if re.match(("^###[^#]"), line) is not None:
                        last_01_md_level_03 = line

                    cur_tokens = num_tokens_from_messages("gpt-3.5-turbo-16k", [{"": '\n'.join(f01_lines)}])
                    f01_new_lines = [line]
                    for s in f01_lines:
                        f01_new_lines.append(s)
                    next_tokens = num_tokens_from_messages("gpt-3.5-turbo-16k", [{"": '\n'.join(f01_new_lines)}])
                    if next_tokens > 1024:
                        print(f"{key} - {total_cnt}")
                        print(f"{last_01_md_level_01}")
                        print(f"{last_01_md_level_02}")
                        print(f"{last_01_md_level_03}")
                        print("BEGIN")
                        filepath_01 = os.path.join(knowledge_dir, f"{dict_databases[key]}-{total_cnt}.md")
                        with open(filepath_01, "w") as f01:
                            for f01_line in f01_lines:
                                f01_line = re.sub("^####", "##### ", f01_line)
                                f01_line = re.sub("^###", "#### ", f01_line)
                                f01_line = re.sub("^##", "### ", f01_line)
                                f01_line = re.sub("^#", "## ", f01_line)
                                f01.write(f01_line)
                        f01_lines = []
                        if last_01_md_level_01 is not None:
                            f01_lines.append(last_01_md_level_01.replace("^#", f"#{total_cnt}  "))
                        if last_01_md_level_02 is not None:
                            f01_lines.append(last_01_md_level_02.replace("^##", f"##{total_cnt}  "))
                        if last_01_md_level_03 is not None:
                            f01_lines.append(last_01_md_level_03.replace("^###", f"###{total_cnt}  "))
                        if re.match(("^#"), line) is None:
                            f01_lines.append(line)
                        total_cnt = total_cnt + 1
                        print("END")
                    else:
                        f01_lines.append(line)
                filepath_01 = os.path.join(knowledge_dir, f"{dict_databases[key]}-{total_cnt}.md")
                with open(filepath_01, "w") as f01:
                    for f01_line in f01_lines:
                        f01.write(f01_line.replace("^####", "##### ").replace("^###", "#### ").replace("^##", "### ").replace("^#", "## "))
                with open(os.path.join(knowledge_dir, f"{dict_databases[key]}.md"), "w") as fw01:
                    fw01.write(f"# {dict_databases[key]}\n")
                    for cnt in range(0, total_cnt):
                        filepath_01 = os.path.join(knowledge_dir, f"{dict_databases[key]}-{cnt}.md")
                        with open(filepath_01, "r") as fr01:
                            for line in fr01.readlines():
                                fw01.write(line)
                with open(os.path.join(knowledge_dir, f"COPY.md"), "a") as fw01:
                    fw01.write(f"# {dict_databases[key]}\n")
                    for cnt in range(0, total_cnt):
                        filepath_01 = os.path.join(knowledge_dir, f"{dict_databases[key]}-{cnt}.md")
                        with open(filepath_01, "r") as fr01:
                            for line in fr01.readlines():
                                fw01.write(line)

        print(msg, " ... OK")

if __name__ == '__main__':
    step07_copy_video().run("")
