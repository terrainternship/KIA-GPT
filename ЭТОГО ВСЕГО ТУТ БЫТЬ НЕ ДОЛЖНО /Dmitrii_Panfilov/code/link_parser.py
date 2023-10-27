# Парсер всех ссылок сайта

import requests
from bs4 import BeautifulSoup
import urllib.parse
from collections import deque
import time
import signal
import sys

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def signal_handler(signal, frame):
    print("\nПроцесс прерван пользователем. Завершение работы...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def collect_internal_links(url, domain, path_prefix):
    visited = set()
    internal_links = set()
    current_level_queue = deque([url])
    next_level_queue = deque()
    save_interval = 10

    print("Начало работы скрипта...\n")

    i = 0
    while current_level_queue or next_level_queue:
        if not current_level_queue:
            current_level_queue, next_level_queue = next_level_queue, current_level_queue

        current_url = current_level_queue.popleft()
        i += 1
        print(f"{i} Проверяется URL: {current_url}")
        
        if current_url in visited:
            continue

        try:
            response = requests.get(current_url, headers=HEADERS, timeout=10, allow_redirects=True)
            response.raise_for_status()
            
            # Если был редирект, добавляем конечный URL в очередь для дальнейшей проверки
            if response.history:
                final_url = response.url
                if domain in final_url and final_url not in visited:
                    current_level_queue.append(final_url)
                    
            soup = BeautifulSoup(response.content, 'html.parser')

            for a_tag in soup.find_all('a', href=True):
                href = a_tag.attrs['href']
                parsed = urllib.parse.urljoin(current_url, href)

                if domain in parsed and parsed not in visited:
                    if parsed.startswith(path_prefix):
                        internal_links.add(parsed)
                    next_level_queue.append(parsed)

            visited.add(current_url)

            if len(internal_links) % save_interval == 0:
                print(f"Временные ссылки сохранены в internal_links_temp.txt")
                save_to_file(internal_links, 'internal_links_temp.txt')

            time.sleep(1)
        except Exception as e:
            print(f"Ошибка при обработке URL {current_url}: {e}")

    return internal_links

def save_to_file(links, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for link in links:
            file.write(f"{link}\n")
    print(f"Ссылки сохранены в {filename}")

def main():
    start_url = "https://www.kia.ru/about"
    domain = urllib.parse.urlparse(start_url).netloc
    path_prefix = f"https://{domain}/about/"
    links = collect_internal_links(start_url, domain, path_prefix)
    save_to_file(links, 'internal_links_final.txt')

if __name__ == "__main__":
    main()
