from step00_create_excel import step00_create_excel
from step01_copy_excel import step01_copy_excel
from step02_parse_website import step02_parse_website
from step03_copy_website import step03_copy_website
from step04_parse_pdf import step04_parse_pdf
from step05_copy_pdf import step05_copy_pdf

if __name__ == '__main__':
    step00_create_excel().run("step00_create_excel")
    step01_copy_excel().run("step01_copy_excel")
    step02_parse_website().run("step02_parse_website")
    step03_copy_website().run("step03_copy_website")
    step04_parse_pdf().run("step04_parse_pdf")
    step05_copy_pdf().run("step05_copy_pdf")