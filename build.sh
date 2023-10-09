#!/bin/sh
cat knowledge/database.txt > ../V.txt
cat knowledge/database.txt > ../VPlusOil.txt
cat knowledge/database.txt > ../VPlusPDF.txt
cat knowledge/database.txt > ../VPlusVideo.txt
cat knowledge/database.txt > ../VPlusDialog.txt
cat knowledge/database.txt > ../VMinusNews.txt
cat knowledge/database.txt > ../FINAL.txt # PlusAllMinusNews.txt

echo >> ../FINAL.txt # PlusAllMinusNews.txt
echo >> ../VPlusOil.txt
echo '# 1' >> ../FINAL.txt # PlusAllMinusNews.txt
echo '# 1' >> ../VPlusOil.txt
cat knowledge/oils.txt >> ../FINAL.txt # PlusAllMinusNews.txt
cat knowledge/oils.txt >> ../VPlusOil.txt

echo >> ../FINAL.txt # PlusAllMinusNews.txt
echo >> ../VPlusPDF.txt
echo '# 2' >> ../FINAL.txt # PlusAllMinusNews.txt
echo '# 2' >> ../VPlusPDF.txt
cat knowledge/pdf_1of4_database.txt >> ../FINAL.txt # PlusAllMinusNews.txt
cat knowledge/pdf_1of4_database.txt >> ../VPlusPDF.txt
cat knowledge/pdf_0of4_database.txt >> ../FINAL.txt # PlusAllMinusNews.txt
cat knowledge/pdf_0of4_database.txt >> ../VPlusPDF.txt
cat knowledge/pdf_2of4_database.txt >> ../FINAL.txt # PlusAllMinusNews.txt
cat knowledge/pdf_2of4_database.txt >> ../VPlusPDF.txt
cat knowledge/pdf_3of4_database.txt >> ../FINAL.txt # PlusAllMinusNews.txt
cat knowledge/pdf_3of4_database.txt >> ../VPlusPDF.txt
cat knowledge/pdf_4of4_database.txt >> ../FINAL.txt # PlusAllMinusNews.txt
cat knowledge/pdf_4of4_database.txt >> ../VPlusPDF.txt

echo >> ../FINAL.txt # PlusAllMinusNews.txt
echo >> ../VPlusVideo.txt
echo '# 3' >> ../FINAL.txt # PlusAllMinusNews.txt
echo '# 3' >> ../VPlusVideo.txt
cat knowledge/video_database_new.txt >> ../FINAL.txt # PlusAllMinusNews.txt
cat knowledge/video_database_new.txt >> ../VPlusVideo.txt

echo >> ../FINAL.txt # PlusAllMinusNews.txt
echo >> ../VPlusDialog.txt
echo '# 4' >> ../FINAL.txt # PlusAllMinusNews.txt
echo '# 4' >> ../VPlusDialog.txt
cat knowledge/dialog_database.txt >> ../FINAL.txt # PlusAllMinusNews.txt
cat knowledge/dialog_database.txt >> ../VPlusDialog.txt
