# -*- coding: utf-8 -*-

class step02_parse_website():
    def __init__(self):
        pass

    def run(self, msg):
        import configparser
        import pathlib
        import shutil
        import os
        config = configparser.ConfigParser()
        config.read('config.txt')
        knowledge_dir = config["DEFAULT"]["knowledge_dir"]
        if knowledge_dir is None: knowledge_dir = "./knowledge"
        pathlib.Path(knowledge_dir).mkdir(parents=True, exist_ok=True)
        prev_knowledge_dir = config["DEFAULT"]["prev_knowledge_dir"]
        if prev_knowledge_dir is None: prev_knowledge_dir = "../knowledge"
        pathlib.Path(prev_knowledge_dir).mkdir(parents=True, exist_ok=True)
        shutil.copyfile(os.path.join(prev_knowledge_dir, "parser_database.txt"), os.path.join(knowledge_dir, "parser_database.txt"))
        """
        import datetime
        import numpy as np
        import openpyxl
        import re
        import requests
        import threading, time
        import json
        import os

        from bs4 import BeautifulSoup



        def savetxt(dir, name, text):
            if not os.path.exists('result'): os.mkdir('result')
            if not os.path.exists('result/' + dir): os.mkdir('result/' + dir)
            with open('result/' + dir + '/' + name, 'w', encoding='utf-8') as f:
                f.write(text)
            return True

        def resulttotext(r):
            if r is not None:
                return r.text + '.'
            else:
                return ''

        def parser(soup):
            text = ''
            pages = soup.findAll('div', class_='g-padding')
            if pages is None:
                print(soup.find('title').text.split(' – ')[0])
                print(soup)
            else:
                for page in pages:
                    if page.find('div', class_='faq') is not None:
                        text += page.find('div', class_='faq').text
                    else:
                        content = page.select('div[class*="text-"]')
                        text += ''.join(i.text + '\n' for i in content)
            return text

        # Pars page whith models

        pagemodels = requests.get('https://www.kia.ru/models/').text
        modellinks = []

        html = ''.join(line.strip() for line in pagemodels.split("\n"))
        soup = BeautifulSoup(html, "html.parser")

        cards_list = soup.find_all('div', class_='car-card')

        for card in cards_list:
            modellinks.append('https://www.kia.ru' + str(card.a['href']))


        def getmodelsoup(url):
            model = requests.get(url).text
            html = ''.join(line.strip() for line in model.split("\n"))
            return BeautifulSoup(html, "html.parser")

        modeldict = {}

        for i in modellinks:
            modeldict[i] = getmodelsoup(i)

        def stringstolist(div):
            '''Превращаем блок в список строк'''
            lis = []
            try:
                for string in div.strings:
                    if string not in [' ', '']:
                        lis.append(string.text)
            except:
                lis = ['']
            return lis

        def parsermodel(soup):
            text = ''

            # Обрабатываю по id basic
            basic = soup.select('div[id*="basic_"]')
            for div in basic:
                # Перевожу строки в список, для удобного обращиния
                textlist = stringstolist(div)
                try:
                    img = div.find('img')['data-src']
                except:
                    img = ''
                text += f'## {textlist[0]}\n{". ".join(textlist[1:])}\nФото {img}\n\n'

            # Обрабатываю по id dizain
            dizain = soup.select('div[id*="dizain_"]')
            for div in dizain:
                if len(div['id'].split('_')) > 2: continue  # Пропускаем внутренние блоки
                # Перевожу строки в список, для удобного обращиния
                textlist = stringstolist(div)[:-1]
                text += f'## {textlist[0]}\n{". ".join(textlist[1:3])}\n'
                for t in textlist[3:]:
                    text += t + '. '
                text = text[:-2] + '\n\n'

            # Обрабатываю по id eksterer
            eksterer = soup.select('div[id*="eksterer_"]')
            for div in eksterer:
                if len(div['id'].split('_')) > 2: continue  # Пропускаем внутренние блоки
                # Перевожу строки в список, для удобного обращиния
                textlist = stringstolist(div)[:-1]
                text += f'## {textlist[0]}\n{". ".join(textlist[1:3])}\n'
                for t in textlist[3:]:
                    text += t + '. '
                text = text[:-2] + '\n\n'

            # Обрабатываю по id interer
            interer = soup.select('div[id*="interer_"]')
            for div in interer:
                if len(div['id'].split('_')) > 2: continue  # Пропускаем внутренние блоки
                # Перевожу строки в список, для удобного обращиния
                textlist = stringstolist(div)[:-1]
                text += f'## {textlist[0]}\n{". ".join(textlist[1:3])}\n'
                for t in textlist[3:]:
                    text += t + '. '
                text = text[:-2] + '\n\n'

            # Обрабатываю по id style
            style = soup.select('div[id*="style_"]')
            for div in style:
                if len(div['id'].split('_')) > 2: continue  # Пропускаем внутренние блоки
                # Перевожу строки в список, для удобного обращиния
                textlist = stringstolist(div)[:-1]
                text += f'## {textlist[0]}\n{". ".join(textlist[1:3])}\n'
                for t in textlist[3:]:
                    text += t + '. '
                text = text[:-2] + '\n\n'

            # Обрабатываю по id multimedia
            multimedia = soup.select('div[id*="multimedia_"]')
            for div in multimedia:
                if len(div['id'].split('_')) > 2: continue  # Пропускаем внутренние блоки
                # Перевожу строки в список, для удобного обращиния
                textlist = stringstolist(div)[:-1]
                text += f'## {textlist[0]}\n{". ".join(textlist[1:3])}\n'
                for t in textlist[3:]:
                    text += t + '. '
                text = text[:-2] + '\n\n'

            # Обрабатываю по id tehnologii
            tehnologii = soup.select('div[id*="tehnologii_"]')
            for div in tehnologii:
                if len(div['id'].split('_')) > 2: continue  # Пропускаем внутренние блоки
                # Перевожу строки в список, для удобного обращиния
                textlist = stringstolist(div)[:-1]
                text += f'## {textlist[0]}\n{". ".join(textlist[1:3])}\n'
                for t in textlist[3:]:
                    text += t + '. '
                text = text[:-2] + '\n\n'

            # Обрабатываю по id bezopasnost
            bezopasnost = soup.select('div[id*="bezopasnost_"]')
            for div in bezopasnost:
                if len(div['id'].split('_')) > 2: continue  # Пропускаем внутренние блоки
                # Перевожу строки в список, для удобного обращиния
                textlist = stringstolist(div)[:-1]
                text += f'## {textlist[0]}\n{". ".join(textlist[1:3])}\n'
                for t in textlist[3:]:
                    text += t + '. '
                text = text[:-2] + '\n\n'

            # Обрабатываю по id teplye_opcii
            teplye_opcii = soup.select('div[id*="teplye_opcii_"]')
            for div in teplye_opcii:
                if len(div['id'].split('_')) > 3: continue  # Пропускаем внутренние блоки
                # Перевожу строки в список, для удобного обращиния
                textlist = stringstolist(div)[:-1]
                text += f'## {textlist[0]}\n{". ".join(textlist[1:3])}\n'
                for t in textlist[3:]:
                    text += t + '. '
                text = text[:-2] + '\n\n'

            # Обрабатываю по id komfort
            komfort = soup.select('div[id*="komfort_"]')
            for div in komfort:
                if len(div['id'].split('_')) > 2: continue  # Пропускаем внутренние блоки
                # Перевожу строки в список, для удобного обращиния
                textlist = stringstolist(div)[:-1]
                text += f'## {textlist[0]}\n{". ".join(textlist[1:3])}\n'
                for t in textlist[3:]:
                    text += t + '. '
                text = text[:-2] + '\n\n'

            # Обрабатываю по id vmestimost
            vmestimost = soup.select('div[id*="vmestimost_"]')
            for div in vmestimost:
                if len(div['id'].split('_')) > 2: continue  # Пропускаем внутренние блоки
                # Перевожу строки в список, для удобного обращиния
                textlist = stringstolist(div)[:-1]
                text += f'## {textlist[0]}\n{". ".join(textlist[1:3])}\n'
                for t in textlist[3:]:
                    text += t + '. '
                text = text[:-2] + '\n\n'

            # Обрабатываю по id dvigatel
            dvigatel = soup.select('div[id*="dvigatel_"]')
            for div in dvigatel:
                if len(div['id'].split('_')) > 2: continue  # Пропускаем внутренние блоки
                # Перевожу строки в список, для удобного обращиния
                textlist = stringstolist(div)[:-1]
                text += f'## {textlist[0]}\n{". ".join(textlist[1:3])}\n'
                text += 'Модели двигателей: '
                ul = div.find('ul')
                for t in stringstolist(ul):
                    text += t + ', '
                text = text[:-2] + '\n\n'

            return text

        def parseroptions(url):
            text = '## Комплектации\n'
            links = []
            url = url.replace('desc', 'options')
            suop = getmodelsoup(url)
            ahrefs = suop.findAll('div', class_='config__variants__slide')
            for a in ahrefs:
                cont = a.find('li').text
                url = a.find('a')
                option = getmodelsoup('https://www.kia.ru' + url['href'])
                titel = option.find('title').text
                text += f'### Комплектация: {titel}\nЦена: {cont}\n'
                info = option.findAll('div', class_="info-section")

                for i in info:
                    t2 = i.find('div', class_="info-section__header").text
                    text += t2 + ': '
                    if t2.strip() == 'Технические характеристики' or t2.strip() == 'Спецификация':
                        dl = i.findAll('dl')
                        for j in dl:
                            text += j.find('dt').text + ': ' + j.find('dd').text + '; '
                    else:
                        li = i.findAll('li')
                        for j in li:
                            text += j.text + ', '
                    text = text[:-2] + '\n'

            return text

        def resultsmodel(link):

            print(link)
            name = modeldict[link].find('title').text.split(' – ')[0]
            name = name.replace('/', '-')
            text = f'#  {name} - [link {link}]\n'
            text += parsermodel(modeldict[link])
            text += parseroptions(link)
            savetxt('models', name + '.txt', text)
            print('Done ' + name)

        threads = []
        # Добавляю потоки с функцией сохранения в файл в список потоков
        for link in modellinks:
            threads.append(threading.Thread(target=resultsmodel, args=(link,)))

        # Технологии

        def parserabout(soup):
            text = '## '
            pages = soup.find('div', class_='articles-detail__technology-txt')
            if pages is None:
                print(soup.find('title').text.split(' – ')[0])
                print(soup)
            else:
                content = pages.select('div[class*="text-"]')
                text += ''.join(i.text + '\n' for i in content)
            return text

        url = "https://www.kia.ru/ajax/page/technologies/more?limit=45&page=1"

        headers = {
            "Referer": "https://www.kia.ru/about/technologies/",  # Example Referer header
        }

        response = requests.get(url, headers=headers)
        json_data = response.text

        data = json.loads(json_data)

        ids = [tech['id'] for tech in data['content']['technologies']]

        static_url = 'https://www.kia.ru/about/technologies/'
        urls = []

        for id in ids:
            urls.append(static_url + id)

        def resultsabout(link):

            print(link)
            content = requests.get(link)
            if content.status_code == 200:
                # constructor-block
                text = ''
                html = ''.join(line.strip() for line in content.text.split("\n"))
                soup = BeautifulSoup(html, "html.parser")
                name = soup.find('title').text.split(' – ')[0]
                text += parserabout(soup)
            savetxt('about', name.replace('/', '-') + '.txt', text)
            print('Done ' + name)

        print(urls)
        for link in urls:
            # Добавляю потоки с функцией сохранения в файл в список потоков
            threads.append(threading.Thread(target=resultsabout, args=(link,)))

        # Сбор с закладки "Журнал"

        url = "https://www.kia.ru/ajax/page/mediacenter/magazine/more?limit=100&page=1"
        static_url = "https://www.kia.ru/press/magazine/"
        HEADERS = {"Referer": static_url}

        response = requests.get(url=url, headers=HEADERS)
        json_data = response.text
        data = json.loads(json_data)
        all_article_list = []

        for article in data["content"]["media_center"]["magazine"]:
            code = article["code"]
            all_article_list.append(static_url + code + '/')

        url = "https://www.kia.ru/ajax/page/mediacenter/news/more?limit=100&page=1"
        static_url = "https://www.kia.ru/press/news/"
        response = requests.get(url=url, headers=HEADERS)
        json_data = response.text
        data = json.loads(json_data)
        all_article_list = []

        for article in data["content"]["media_center"]["news"]:
            code = article["code"]
            all_article_list.append(static_url + code + '/')

        def resultspress(link):

            print(link)
            content = requests.get(link)
            if content.status_code == 200:
                # constructor-block
                text = ''
                html = ''.join(line.strip() for line in content.text.split("\n"))
                soup = BeautifulSoup(html, "html.parser")
                name = soup.find('title').text.split(' – ')[0]
                head_press = soup.h1.text.strip()  # заголовок статьи
                all_img_list, all_img = [], ""
                try:
                    [all_img_list.append(img.find("img").attrs.get("src")) for img in
                     soup.find_all("div", class_="articles-detail__content__offset")]  # все фото из статьи
                    for img in all_img_list:
                        all_img += img + ","
                except:
                    all_img = ""

                try:
                    date_press = soup.select_one("div.articles-detail__date").text.strip()  # дата статьи
                    for val in soup.find_all("div", class_="g-container"):
                        for child in val.children:
                            if date_press in child.text:
                                text += f"## {head_press}>\n"
                                text += child.text.replace("\xa0", " ")
                                text += f"\nФотографии из статьи: {all_img[:-1]}\n\n"
                except:
                    for val in soup.find_all("div", class_="g-container"):
                        for child in val.children:
                            if child.find("h1") is not None and child.find("h1") != -1:
                                text += f"## {head_press}\n"
                                text += child.text.replace("\xa0", " ")
                                text += f"\nФотографии из статьи: {all_img[:-1]}\n\n"
                if text != '':
                    savetxt('press', name.replace('/', '-') + '.txt', text)
                    print('Done ' + name)

        # threads = []
        for link in all_article_list:
            threads.append(threading.Thread(target=resultspress, args=(link,)))

        # Start all threads
        for x in threads:
            x.start()
            time.sleep(0.5)

        # Wait for all of them to finish
        for x in threads:
            x.join()

        # Тест ассортимента

        base_url = "https://www.kia.ru/ajax/page/accessories/filter?sort=sort&order=desc&page=1"

        headers = {
            "Referer": "https://www.kia.ru/service/accessories/",  # Example Referer header
        }

        bigdata = []

        start_page = 1

        while True:
            current_url = base_url + str(start_page)
            response = requests.get(current_url, headers=headers)
            json_data = response.text
            data = json.loads(json_data)
            if len(data['content']['accessories']) == 0: break

            for tech in data['content']['accessories']:
                bigdata.append(tech)

            start_page += 1

        text = '# Аксесуары\n'
        for i in bigdata:
            if i['material'] == '':
                i['material'] = {}
                i['material']['name'] = ''
            text += f'## Наименование: {i["name"].strip()}, Фото: https://cdn.kia.ru/resize/1295x632{i["image"]},'
            text += f'Артикул: {i["article"]}, Материал: {i["material"]["name"].strip()}.\n{i["text"]}'
            if i['technical_features'] is not None:
                html = ''.join(line.strip() for line in i['technical_features'].split("\n"))
                soup = BeautifulSoup(html, "html.parser")
                technical_features = '. '.join(soup.strings)
            text += technical_features + '\n'
        savetxt('accessories', 'accessories.txt', text)

        # Test oil page
        oil_res = {}
        headers = {"Referer": 'https://www.kia.ru/'}

        json_data = json.loads(requests.get('https://www.kia.ru/ajax/decoder/model_lines',
                                            headers={"Referer": 'https://www.kia.ru/'}).text)
        model_lines = list(json_data['content']['model_lines'])
        print(datetime.datetime.now())
        for id in model_lines:
            try:
                model_line_id = id['id']
                json_data = json.loads(requests.get('https://www.kia.ru/ajax/decoder/years',
                                                    params={'model_line_id': model_line_id},
                                                    headers=headers).text)
                years = list(json_data['content']['years'])
                for year in years:
                    year = year['id']
                    json_data = json.loads(requests.get('https://www.kia.ru/ajax/decoder/models',
                                                        params={'model_line_id': model_line_id, 'year': year},
                                                        headers=headers).text)
                    models = list(json_data['content']['models'])
                    for model in models:
                        model_id = model['id']
                        json_data = json.loads(requests.get('https://www.kia.ru/ajax/decoder/complectations',
                                                            params={'model_id': model_id},
                                                            headers=headers).text)
                        complectations = list(json_data['content']['complectations'])
                        for complectation in complectations:
                            complectation_id = complectation['id']
                            json_data = json.loads(
                                requests.get('https://www.kia.ru/ajax/page/oils/complectations/' + complectation_id,
                                             headers=headers).text)
                            oils = list(json_data['content']['oils'])
                            car = json_data['content']['car']
                            if oils != []:
                                for oil in oils:
                                    com_name = car['model']['model_line']['name'] + ' '
                                    com_name += car['model']['generation']['name'] + '/ ' + str(year) + '/ '
                                    com_name += car['model']['carcass']['name'] + '/ '
                                    com_name += str(car['modification']['engine']['engine_volume']) + ' '
                                    com_name += car['modification']['engine']['engine_type'] + '/ '
                                    com_name += car['modification']['engine']['fuel_type'] + '/ '
                                    com_name += car['modification']['transmission']['drive'] + '/ '
                                    com_name += car['modification']['transmission']['gearbox'] + '/ '

                                    if not oil['name'] in oil_res.keys():
                                        oil_res[oil['name']] = [oil['description'], com_name]
                                    else:
                                        oil_res[oil['name']] += [com_name]
            except Exception as e:
                print(e)
        print(oil_res)
        print(datetime.datetime.now())


        url = "https://www.kia.ru/kiaflex/"
        response = requests.get(url=url, headers=HEADERS).text
        html = ''.join(line.strip() for line in response.split("\n"))
        soup = BeautifulSoup(html, "html.parser")

        savetxt('kiaflex', 'kiaflex.txt', '# ' + parser(soup))

        for oil in oil_res:
            print(oil, oil_res[oil][0])
        """

        """!echo "# Технологии" > database.txt"""
        """!cat result/about/*.txt >> database.txt"""
        """!cat result/press/*.txt >> database.txt"""
        """!cat result/models/*.txt >> database.txt"""
        """!cat result/kiaflex/*.txt >> database.txt"""
        """!cat result/accessories/*.txt >> database.txt"""
        """!zip -r result.zip result database.txt"""
        """!zip database.zip database.txt"""

        print(msg, " ... OK")

if __name__ == '__main__':
    step02_parse_website().run("")
