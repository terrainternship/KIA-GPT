# Функция очистки ссылок
import re

def clean_youtube_url(url: str) -> str:
    """
    Преобразует любую ссылку на видео YouTube в формат короткой ссылки (https://youtu.be/ID_ВИДЕО).

    Параметры:
        url (str): Исходная ссылка на видео на YouTube.

    Возвращает:
        str: Короткая ссылка на видео или None, если исходная ссылка не соответствует формату YouTube.

    Пример:
        >>> clean_youtube_url("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        "https://youtu.be/dQw4w9WgXcQ"
    """

    # Регулярное выражение для поиска идентификаторов видео YouTube:
    # 1. (?:https?:\/\/)? - необязательный протокол (http или https).
    # 2. (?:www\.)? - необязательный префикс "www".
    # 3. (?:youtube\.com\/(?:watch\?v=|embed\/)|youtu\.be\/) - паттерн для длинных (стандартных и embed) и коротких ссылок YouTube.
    # 4. ([a-zA-Z0-9_-]{11}) - идентификатор видео, состоящий из 11 символов.
    pattern = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:watch\?v=|embed\/)|youtu\.be\/)([a-zA-Z0-9_-]{11})"

    # Поиск совпадения с помощью регулярного выражения
    match = re.search(pattern, url)
    if match:
        # Если найдено совпадение, извлекаем идентификатор видео
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    else:
        return None
