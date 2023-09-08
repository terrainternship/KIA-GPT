from clean_youtube_url import clean_youtube_url
from download_video import download_video
from transcribe_audio_files import transcribe_audio_files

# Установка yt-dlp
!pip install -q yt-dlp
# Установка whisper
!pip install -q git+https://github.com/openai/whisper.git

# Список ссылок для загрузки
urls_list = [
    "https://youtu.be/ih_B0-Y9gNE",
    "https://youtu.be/6DG5gzCXoRg?list=TLGGjOElj14_uCEyNTA4MjAyMw",
    "https://youtu.be/V1rcD1gDu9k",
    "https://www.youtube.com/embed/ih_B0-Y9gNE?iv_load_policy=3&autoplay=1&rel=0&version=3&loop=1&playlist=ih_B0-Y9gNE"
]

# Перебор каждой очищенной ссылки из списка cleaned_urls.
# Для каждой ссылки будет вызвана функция download_video,
# которая загрузит видео в формате m4a и сохранит его в директории /content/audios/.
for url in cleaned_urls:
    download_video(url)

transcribe_audio_files('/content/audios', '/content/out')

!ls -ahl ./audios
! ls -ahl ./out
