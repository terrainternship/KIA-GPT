Tutorial pro telegram bot: https://goo.su/Anp6
PDF: https://goo.su/uirUv4n
Article: https://code.visualstudio.com/docs/containers/ssh
Hosting: https://console.cloud.yandex.com

![Screenshot_1](https://github.com/terrainternship/KIA-GPT/assets/29410375/5e71b38c-86d6-448f-a5db-f7635930313e)

https://docs.github.com/en/actions/publishing-packages/publishing-docker-images

https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

`
>>>, [15.10.2023 17:43]
Как в проекте на github, в котором лежат requirements.txt и Dockerfile создать tag для релиза. Распиши по шагам инструкцию.
`

`
ChatGPT для Telegram, [15.10.2023 17:43]
Конечно! Вот пошаговая инструкция по развертыванию файлов requirements.txt и Dockerfile на виртуальной машине Yandex Compute Cloud с использованием образа на Yandex Container Registry:

Шаг 1: Создание и настройка виртуальной машины Yandex Compute Cloud
1. Создайте виртуальную машину в Yandex Compute Cloud, настроив все необходимые параметры (размер машины, регион и т.д.). Обратите внимание, что виртуальная машина должна иметь доступ в интернет.

Шаг 2: Загрузка образа на Yandex Container Registry
1. Зайдите в Yandex Container Registry и создайте репозиторий для образа. Укажите все необходимые настройки, такие как имя репозитория и приватность (публичный или приватный доступ).
2. Загрузите Docker-образ на Yandex Container Registry с помощью команды `docker push`. Например, для образа с именем `my-image` и тегом `v1`, выполните команду `docker push <registry>/<repo>/<image>:<tag>`. Замените `<registry>` на URL Yandex Container Registry, `<repo>` на имя репозитория, `<image>` на имя образа и `<tag>` на желаемый тег.

Шаг 3: Развертывание образа на виртуальной машине
1. Подключитесь к виртуальной машине Yandex Compute Cloud, используя SSH или другой метод удаленного доступа.
2. Установите Docker на виртуальную машину с помощью команды `sudo apt-get update && sudo apt-get install -y docker.io`.
3. Скопируйте файлы requirements.txt и Dockerfile в директорию на виртуальной машине.
4. Склонируйте репозиторий с образом Docker с Yandex Container Registry на виртуальную машину, используя команду `docker pull <registry>/<repo>/<image>:<tag>`. Замените `<registry>` на URL Yandex Container Registry, `<repo>` на имя репозитория, `<image>` на имя образа и `<tag>` на ранее загруженный тег.
5. Соберите Docker-образ на виртуальной машине с помощью команды `docker build -t <image_name> -f Dockerfile .`. Замените `<image_name>` на имя, которое вы хотите присвоить образу.
6. Запустите контейнер из собранного образа с помощью команды `docker run -d -p <host_port>:<container_port> <image_name>`, где `<host_port>` - порт на виртуальной машине, который будет проксироваться к контейнеру, и `<container_port>` - порт, на котором работает приложение в контейнере.

После завершения всех шагов приложение, описанное в файле Dockerfile, будет развернуто на виртуальной машине Yandex Compute Cloud с использованием образа из Yandex Container Registry.
`
