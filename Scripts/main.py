from step00_create_excel import step00_create_excel
from step01_copy_excel import step01_copy_excel
from step02_parse_website import step02_parse_website
from step03_copy_website import step03_copy_website
from step04_parse_pdf import step04_parse_pdf
from step05_copy_pdf import step05_copy_pdf
from step06_parse_video import step06_parse_video
from step07_copy_video import step07_copy_video
from step08_parse_summary import step08_parse_summary
from step09_copy_summary import step09_copy_summary
from step10_refactor_excel import step10_refactor_excel
from step11_refactor_website import step11_refactor_website
from step12_refactor_pdf import step12_refactor_pdf
from step13_refactor_video import step13_refactor_video
from step14_refactor_summary import step14_refactor_summary
from step15_separate_trash import step15_separate_trash
from step16_import_weights import step16_import_weights
from step17_mmralgo_examination import step17_mmralgo_examination

if __name__ == '__main__':
    step00_create_excel().run("step00_create_excel")
    step01_copy_excel().run("step01_copy_excel")
    step02_parse_website().run("step02_parse_website")
    step03_copy_website().run("step03_copy_website")
    step04_parse_pdf().run("step04_parse_pdf")
    step05_copy_pdf().run("step05_copy_pdf")
    step06_parse_video().run("step06_parse_video")
    step07_copy_video().run("step07_copy_video")
    step08_parse_summary().run("step08_parse_summary")
    step09_copy_summary().run("step09_copy_summary")
    step10_refactor_excel().run("step10_refactor_excel")
    step11_refactor_website().run("step11_refactor_website")
    step12_refactor_pdf().run("step12_refactor_pdf")
    step13_refactor_video().run("step13_refactor_video")
    step14_refactor_summary().run("step14_refactor_summary")
    step15_separate_trash().run("step15_separate_trash")
    step16_import_weights().run("step16_import_weights")
    step17_mmralgo_examination().run("step17_mmralgo_examination")
