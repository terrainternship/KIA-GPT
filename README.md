# KIA-GPT
ТУТ БУДЕТ ОПИСАНИЕ


--- 
## База знаний
База знаний для Нейро-консультанта : `knowledge/database.md`

Это документ, который используется для поиска необходимой информации по запросу пользователя.
Изменять его необходимо крайне осторожно, соблюдая структуру файла в формате MarkDown

---

# Установка сервера 

Используется Ubuntu 22.04. Все действия делаем в консоле сервера

1. Обновляем систему

`sudo apt update`

2. Устанавливаем Python

`sudo apt install python3`

3. Устанавливаем pip

`sudo apt install python3-pip`

4. Устанавливаем venv

`sudo apt install python3-venv`

5. Создаем виртуальную среду и активируем

`python -m venv venv`

`source venv/bin/activate`

6. Загружаем каталог с проектом
7. Переходим в него

`cd <Имя папки с проектом>`

# Установка библиотек
Вводим эту команду в консоле для установке в среде.

`pip install -r requirements.txt`

# Запуск 

`python main.py`