# Скрипт загрузки всех медиа файлов со странице
# поиск по атрибутам, а не content-type —> требуется доработка

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_absolute_url(base_url, link):
    return urljoin(base_url, link)

def extract_media_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    media_links = []

    # Извлечение ссылок на изображения
    for img in soup.find_all('img', {'src': True}):
        media_links.append(get_absolute_url(url, img['src']))
    
    for img in soup.find_all('img', {'data-src': True}):
        media_links.append(get_absolute_url(url, img['data-src']))

    # Извлечение ссылок на видео
    for video in soup.find_all('video', {'src': True}):
        media_links.append(get_absolute_url(url, video['src']))
    
    for video in soup.find_all('video', {'data-src': True}):
        media_links.append(get_absolute_url(url, video['data-src']))

    # Извлечение favicon
    link_element = soup.find("link", rel="icon")
    if link_element:
        favicon_link = link_element.get("href")
        if favicon_link:
            media_links.append(get_absolute_url(url, favicon_link))

    # Уникальные медиа-ссылки
    media_links = list(set(media_links))
    
    return media_links

def save_media_files(media_links, download_folder="downloaded_media"):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    for link in media_links:
        try:
            response = requests.get(link, stream=True)
            filename = os.path.join(download_folder, os.path.basename(link))
            
            with open(filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        except Exception as e:
            print(f"Не удалось скачать {link}. Ошибка: {e}")

def main():
    url = "https://www.kia.ru/models/cerato/desc/"  # input("Введите URL страницы: ")
    media_links = extract_media_links(url)
    save_media_files(media_links)
    print(f"Медиа файлы сохранены в папку 'downloaded_media'.")

if __name__ == "__main__":
    main()
