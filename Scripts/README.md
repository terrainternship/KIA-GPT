* step00_create_excel.py - готовит эксель для самых важных данных (текущие цены, стоимость аренды и т д)
* step01_copy_excel.py - строит из эксель первую базу знаний раздела # 0
* step02_parse_website.py - парсит страницы веб сайта
* step03_copy_website.py - добавляет разделы вебсайта в раздел # 1
* step04_parse_pdf.py - парсит pdf веб сайта
* step05_copy_pdf.py - добавляет разделы pdf в раздел # 2
* step06_parse_video.py - парсит video веб сайта
* step07_copy_video.py - добавляет разделы pdf в раздел # 3
* step08_parse_summary.py - парсит summary диалогов
* step09_copy_summary.py - добавляет разделы диалогов в раздел # 4
* step10_refactor_excel.py - разбивает разделы эксель на разделы похожие с example
* step11_refactor_website.py - разбивает разделы вебсайта на разделы похожие с example
* step12_refactor_pdf.py - разбивает разделы pdf на разделы похожие с example
* step13_refactor_video.py - разбивает разделы video на разделы похожие с example
* step14_refactor_summary.py - разбивает разделы диалогов на разделы похожие с example
* step15_separate_trash.py - находит схожие разделы и маркирует мусор
* step16_import_weights.py - импортирует веса из таблиц тестирования
* step17_mmralgo_exam.py - выборочно корректирует веса нейро экзаменатором