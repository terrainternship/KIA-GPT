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

5. Загружаем каталог с проектом
`git clone -b collab_most_die https://github.com/TasksAndreySorokin/KIA-GPT1.git`

6. Переходим в него

`cd KIA-GPT1`

7. Создаем виртуальную среду и активируем

`python -m venv venv`

`source venv/bin/activate`

# Установка библиотек
Вводим эту команду в консоле для установке в среде.

`pip install -r requirements.txt`

# Запуск 

`python main.py`