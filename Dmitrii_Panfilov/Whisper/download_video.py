# Функция загрузки видео в формате m4a (аудиофайл) с YouTube в директоррию /content/videos/
import subprocess

def download_video(url: str) -> None:
    """
    Загружает видео с YouTube в формате m4a (аудиофайл) и сохраняет в директории /content/audios/.

    Параметры:
        url (str): Ссылка на видео на YouTube.

    Пример:
        >>> download_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        ...
    """

    # Команда для yt-dlp, которая:
    # 1. Использует опцию "-x" для извлечения аудио.
    # 2. Устанавливает формат аудио в "m4a".
    # 3. Определяет путь для сохранения файла.
    cmd = [
        "yt-dlp",
        "-x",
        "--audio-format", "m4a",
        "-o", "/content/audios/%(title)s.%(ext)s",
        url
    ]

    try:
        # Инициализация подпроцесса с заданной командой.
        # stdout=subprocess.PIPE позволяет читать вывод в реальном времени.
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        # Чтение вывода команды в реальном времени и его вывод на экран.
        for line in process.stdout:
            print(line.strip())

        # Ожидание завершения подпроцесса и получение кода завершения.
        return_code = process.wait()

        # Если процесс завершился с ошибкой (не нулевой код завершения), генерируем исключение.
        if return_code != 0:
            raise subprocess.CalledProcessError(return_code, cmd)

    # Обработка исключений при выполнении команды.
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при обработке ссылки {url}:")
        print(str(e))


