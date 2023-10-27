## 💠 Проект Киа "Создание нейро-консультанта для ответов на вопросы клиентов"
![image](https://github.com/terrainternship/KIA-GPT/assets/99917230/2a432b89-43ab-4a3d-8c17-b9563cf96457)


<details>
    <summary><h2>💾 Ссылки на материалы</h2></summary><p>
<li><strong><a href="https://raw.githubusercontent.com/terrainternship/KIA-GPT/main/Dmitrii_Panfilov/Kia_Solution_Model_v40.pdf">⚙️ Схема Интеграции Решения в Прод</a></strong></li>
<li><strong><a href="https://raw.githubusercontent.com/terrainternship/KIA-GPT/main/Dmitrii_Panfilov/Kia_БЗ_v21.md">💾 База Знаний (автоматического парсинга сайта) v.21</a></strong></li>
<li><strong><a href="https://colab.research.google.com/drive/1E-zR2zCRih5XkmhqL592cmijf1jWv-6S?usp=sharing">🗣 Whisper Транскрибация [Google Colab Notebook]</a></strong></li>
<li><strong><a href="https://drive.google.com/file/d/1FIt8qR5-ZGaVwmUwRKSqgbfhz6h-aIDf/view?usp=sharing">🌐Ссылка на архив с обработанными видео-файлами [Google Drive]</a></strong></li>
</p>
</details>

---

<details><summary><h3>🗣 Пример Whisper Транскрибация</h3></summary><p>
<li><strong><a href="https://colab.research.google.com/drive/1E-zR2zCRih5XkmhqL592cmijf1jWv-6S?usp=sharing">Google Colab Notebook</a></strong></li><br>
<img src="https://github.com/terrainternship/KIA-GPT/assets/99917230/b89d1c06-6006-4fc8-a6bf-a51350207f66" alt="image" />
</p></details>

---

<details><summary><h2>📆 Промежуточные результаты на [19.08.2023]</h2></summary>
    <h3>🔘 [19.09.2023]: Разработка схемы интеграции решения в прод</h3>
<li>1. Анализ подходов для интгерации подобных решений на рынке с учетом ТЗ заказчика</li>
<li>2. Разработка схемы интеграции решения в прод, выделение основных этапов внедрения</li>
    <h3>🔘 [12.09.2023]: Приведение кода по Транскрибации к формату Google Colab</h3>
<li>1. Подготовка Google Colab Notebook для транскрибации [Whisper]</li>
<li>2. Поиск в ручном режиме ссылок на Видео (запрещенных для парсинга), транскрибация неохваченных видео в автоматическом режиме</li>
    <h3>🔘 [07.09.2023]: Транскрибация и Суммаризация Видео по ограниченному ТЗ списку</h3><p>
<li>1. Окончательная транскрибация всех найденных видео компании Киа</li>
<li>2. Создание Базы Знаний в виде файла Markdown с добавлением ссылок на изображение и транскрибированного текста (11 видео из заданного списка). Из 86 ссылок в ТЗ запрещены к парсингу 16 ссылок, а 8 - несуществующие!</li>
<li>3. Создание пилотного Телеграм-Бота для обработки pdf-файлов с возможностью суммаризации</li>
    <br>
    <h3>🔘 [31.08.2023]: Транскрибация и Суммаризация Видео</h3>
<li>1. Найдено <b>390 видео по Киа</b>, из которых выделялись аудио-дорожки</li>
<li>2. Проведен сравнительный анализ методов транскрибации аудио (преобразование в текстовый формат): <b>Субтитры с Youtube, Тиньков, Whisper (LARGE vs LARGE_v2)</b></li>
<li>3. Выполнена <b>транскрибация</b> для 390 аудио файлов</li>
<li>4. Проведен экспресс-анализ методов суммаризации ("конденсация текста"): <b>chatGPT, Hugging Face Transformers, модели Сбера (ruBERT и online API)</b></li>
<li>5. Выполнена <b>суммаризация всех полученных текстов</b> с представлением нескольких вариантов в формате JSON через <b>online API модель Сбера</b> (с выделением варианта <b>Best</b>)</li>
<br>
</p></details>

---

<details><summary><h2>🪬 Техническое задание</h2></summary><p>
<h3>🌐 Источники:</h3>
<li><b><a href="https://docs.google.com/spreadsheets/d/1UDwTDX41NHL626aZpLGO4yvYDvX4P_wfL20kv6ekbD8/edit?usp=sharing">Диалоги оператор + клиент</a></b></li>
<li><b><a href="https://docs.google.com/spreadsheets/d/1btiLDeliT87fFw4yI4aFMEthwL0GtUFMKAgGDW6ryOk/edit?usp=sharing">Список страниц</a></b></li>
<h3>💎 Цель проекта:</h3> 
<b>👁‍🗨 Создать нейро-консультанта, отвечающего на вопросы клиентов организации по продуктам и услугам компании.</b>
<h3>🗒 Основные задачи:</h3>
<h4>1. Подготовка базы знаний:</h4>
<li>Сбор базы знаний (на основе представленных заказчиком ссылок и документов)</li>
<li>оптимизация структуры базы знаний</li>
<li>разделение базы знаний на логические блоки</li>
‌<h4>2. Составление алгоритма с дообучением ChatGPT. Проработка механизма ведения диалога</h4>
<h4>3. Тестирование алгоритма:</h4>
<li>создание пула вопросов для тестирования</li>
<li>тестирование алгоритма</li>
<li>корректировка базы знаний и алгоритма</li>
<h4>4. Внедрение и тестирование:</h4>
<li>Интеграция нейро-консультанта по согласованию с заказчиком</li>
<li>Проведение тестирования и отладки системы</li>
<h3>🔰 Ожидаемые результаты:</h3>
<li><b>🤖 Нейро-консультант, отвечающий на вопросы клиентов компании по продуктам и услугам.</b></li>
<li>‌<b>📆 Сроки проекта: 3 месяца</b></li>
</p></details>

---

<details><summary>Прочее</summary>
### 📡 Запуск

1. Установка зависимости:
   ```bash
   pip install -r requirements.txt

2. Для обучения:
   ```bash
   python3 algorithm/chatgpt_training.py
</details>
