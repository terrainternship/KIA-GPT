from step00_create_excel import step00_create_excel
from step01_build_excel import step01_build_excel
from step02_parse_website import step02_parse_website

if __name__ == '__main__':
    step00_create_excel().run("step00_create_excel")
    step01_build_excel().run("step01_build_excel")
    step02_parse_website().run("step02_parse_website")
