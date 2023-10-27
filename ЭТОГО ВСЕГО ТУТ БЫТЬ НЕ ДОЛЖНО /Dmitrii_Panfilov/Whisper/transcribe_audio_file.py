import os
from typing import List

def _construct_whisper_command(input_path: str, output_dir: str) -> List[str]:
    """
    Формирование команды для программы whisper.

    Args:
    - input_path (str): Путь к исходному аудиофайлу.
    - output_dir (str): Путь к директории, где сохранить результаты транскрибации.

    Returns:
    - List[str]: Список аргументов для команды whisper.

    Команда whisper используется для автоматической транскрибации аудиозаписей.
    В данной функции мы формируем список аргументов для этой команды:
    1. `--model large-v2`: использование улучшенной большой модели (версии 2) для транскрибации.
    2. `--language ru`: указание языка речи на русском.
    3. `--device cuda`: использование графического процессора (GPU) для ускорения транскрибации.
    4. `--output_format txt`: формат вывода результатов транскрибации в текстовом файле.
    """
    return [
        'whisper',
        input_path,
        '--model', "large-v2",
        '--language', 'ru',
        '--device', 'cuda',
        '--output_format', 'all',
        '--output_dir', output_dir
    ]


def transcribe_audio_files(input_directory: str, output_directory: str) -> None:
    """
    Транскрибирование всех аудиофайлов из указанной директории с помощью whisper.

    Args:
    - input_directory (str): Директория с исходными аудиофайлами.
    - output_directory (str): Директория для сохранения результатов транскрибации.

    Для каждого файла из `input_directory` запускается процесс транскрибации.
    Результаты сохраняются в поддиректории `output_directory`, где каждая поддиректория соответствует одному аудиофайлу.
    """

    # Проверка наличия выходной директории и её создание при отсутствии
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Формирование списка аудиофайлов с расширением .m4a
    files = [f for f in os.listdir(input_directory) if os.path.isfile(os.path.join(input_directory, f)) and f.endswith('.m4a')]

    # Для каждого аудиофайла:
    for file in files:
        input_path = os.path.join(input_directory, file)

        # Имя поддиректории формируется на основе имени файла без расширения
        subdir_name = os.path.splitext(file)[0]
        subdir_path = os.path.join(output_directory, subdir_name)

        # Информирование пользователя о текущем файле
        print(f"Транскрибирование файла: {file}...")

        # Формирование команды для whisper
        cmd = _construct_whisper_command(input_path, subdir_path)

        # Запуск процесса транскрибации и вывод результатов в реальном времени
        with subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True) as process:
            for line in iter(process.stdout.readline, ''):
                print(line, end='')  # Вывод строки в реальном времени
            print(f"\nТранскрибирование файла {file} завершено.")
