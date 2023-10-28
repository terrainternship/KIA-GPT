step00_create_excel.py - готовит эксель для самых важных данных (текущие цены, стоимость аренды и т д)
step01_build_excel.py - строит из эксель первую базу знаний раздела # 0
step02_parse_website.py - парсит страницы веб сайта
step03_append_website.py - добавляет разделы вебсайта в раздел # 1
step04_parse_pdf.py - парсит pdf веб сайта
step05_append_pdf.py - добавляет разделы pdf в раздел # 2
step06_parse_video.py - парсит video веб сайта
step07_append_video.py - добавляет разделы pdf в раздел # 3
step08_parse_summary.py - парсит summary диалогов
step09_append_summary.py - добавляет разделы диалогов в раздел # 4
step10_refactor_excel.py - разбивает разделы эксель на разделы example
step11_refactor_website.py - разбивает разделы вебсайта на разделы example
step12_refactor_pdf.py - разбивает разделы pdf на разделы example
step13_refactor_video.py - разбивает разделы video на разделы example
step14_refactor_summary.py - разбивает разделы диалогов на разделы example
step15_separate_trash.py - находит схожие разделы и маркирует мусор
step16_import_weights.py - импортирует веса из таблиц тестирования
step17_neuro_examination.py - выборочно корректирует веса нейро экзаменатором