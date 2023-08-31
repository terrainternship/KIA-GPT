# парсер страниц /about/technologies/

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_absolute_url(base_url, link):
    return urljoin(base_url, link)

def extract_content_and_media(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Извлечение текста из div по классу articles-detail
    div_element = soup.find('div', class_='articles-detail')
    text_content = div_element.get_text() if div_element else None

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

    # Уникальные медиа-ссылки
    media_links = list(set(media_links))
    
    return text_content, media_links

def main():
    url = "https://www.kia.ru/about/technologies/f4960620-1702-457a-99df-485f60ceeee9/"  # input("Введите URL страницы: ")
    text_content, media_links = extract_content_and_media(url)

    if text_content:
        with open('articles_detail.txt', 'w', encoding='utf-8') as text_file:
            text_file.write(text_content)
        print("Текст сохранен.")

    if media_links:
        with open('media_links.txt', 'w', encoding='utf-8') as media_file:
            for link in media_links:
                media_file.write(link + '\n')
        print("Ссылки на медиа сохранены.")

if __name__ == "__main__":
    main()
