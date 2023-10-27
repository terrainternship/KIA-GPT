# Общий парсер всего текста со страницы
# также достаёт ссылки на медиа

import requests
from bs4 import BeautifulSoup

def extract_media_and_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    media_links = []

    # Извлечение ссылок на изображения
    for img in soup.find_all('img', {'src': True}):
        media_links.append(img['src'])
    
    for img in soup.find_all('img', {'data-src': True}):
        media_links.append(img['data-src'])

    # Извлечение ссылок на видео
    for video in soup.find_all('video', {'src': True}):
        media_links.append(video['src'])
    
    for video in soup.find_all('video', {'data-src': True}):
        media_links.append(video['data-src'])

    # Извлечение текста со страницы
    text_content = soup.get_text()

    return media_links, text_content

def save_to_files(media_links, text_content):
    with open('media_links.txt', 'w', encoding='utf-8') as media_file:
        for link in media_links:
            media_file.write(link + '\n')

    with open('text.txt', 'w', encoding='utf-8') as text_file:
        text_file.write(text_content)

def main():
    url = "https://www.kia.ru/models/cerato/desc/"  #input("Введите URL страницы: ")
    media_links, text_content = extract_media_and_text(url)
    save_to_files(media_links, text_content)
    print("Данные сохранены.")

if __name__ == "__main__":
    main()
