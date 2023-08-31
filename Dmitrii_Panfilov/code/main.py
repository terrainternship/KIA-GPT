#!WARNING Код требует дорабки
"""
- Зависает при большом кол-ве ссылок
- Ходит рекурсивно начиная с главной страницы (реализовать subpath парсинг)
"""

import requests
from bs4 import BeautifulSoup
import urllib.parse
from collections import deque
import time

def collect_internal_links(url, domain):
    visited = set()
    internal_links = set()
    queue = deque([url])
    save_interval = 40  # Сохраняем каждые 40 ссылок

    while queue:
        current_url = queue.popleft()

        if current_url in visited:
            continue

        try:
            response = requests.get(current_url)
            soup = BeautifulSoup(response.content, 'html.parser')

            for a_tag in soup.find_all('a', href=True):
                href = a_tag.attrs['href']
                parsed = urllib.parse.urljoin(current_url, href)
                if domain in parsed and parsed not in visited:
                    internal_links.add(parsed)
                    queue.append(parsed)

            visited.add(current_url)

            # Промежуточное сохранение
            if len(internal_links) % save_interval == 0:
                save_to_file(internal_links, 'internal_links_temp.txt')

            time.sleep(1)  # Задержка в 1 секунду
        except Exception as e:
            print(f"Ошибка при обработке URL {current_url}: {e}")

    return internal_links

def save_to_file(links, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for link in links:
            file.write(f"{link}\n")
    print(f"Ссылки сохранены в {filename}")

def main():
    start_url = "https://www.kia.ru/about"  # input("Введите стартовый URL (например, https://example.com): ")
    domain = urllib.parse.urlparse(start_url).netloc
    links = collect_internal_links(start_url, domain)
    save_to_file(links, 'internal_links_final.txt')

if __name__ == "__main__":
    main()
