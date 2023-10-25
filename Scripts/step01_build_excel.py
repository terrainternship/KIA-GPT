# -*- coding: utf-8 -*-

class step01_build_excel():
    def __init__(self):
        pass

    def run(self, msg):
        # 1. Автомобили Kia в кредит - расчитать кредит на покупку https://www.kia.ru/buy/calc/
        # 2. Расчет стоимости ТО - https://www.kia.ru/service/calculator_to/
        # 3. Программа Trade-In - https://www.kia.ru/buy/trade-in/
        EXCEL_TEXT = ""
        import configparser
        import pathlib
        import os
        config = configparser.ConfigParser()
        config.read('config.txt')
        knowledge_dir = config["DEFAULT"]["knowledge_dir"]
        if knowledge_dir is None: knowledge_dir = "./knowledge"
        pathlib.Path(knowledge_dir).mkdir(parents=True, exist_ok=True)
        filepath_01 = os.path.join(knowledge_dir, "__01_calc_credit_database.txt")
        with open(filepath_01, "w") as f01:
            f01.write("")
        filepath_02 = os.path.join(knowledge_dir, "__02_calc_tech_database.txt")
        with open(filepath_02, "w") as f02:
            f02.write("")
        filepath_03 = os.path.join(knowledge_dir, "__03_calc_tradein.txt")
        with open(filepath_03, "w") as f03:
            f03.write("")
        print(msg, " ... OK")

if __name__ == '__main__':
    step01_build_excel().run("")
