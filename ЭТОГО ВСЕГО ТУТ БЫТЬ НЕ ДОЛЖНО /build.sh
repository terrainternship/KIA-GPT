#!/bin/sh
cat knowledge/database.txt > ../V.txt
cat knowledge/database.txt > ../VPlusOil.txt
cat knowledge/database.txt > ../VPlusPDF.txt
cat knowledge/database.txt > ../VPlusVideo.txt
cat knowledge/database.txt > ../VPlusDialog.txt
cat knowledge/database.txt > ../VPlusNews.txt
cat knowledge/database.txt > ../VPlusAllMinusNews.txt

echo >> ../VPlusAllMinusNews.txt
echo >> ../VPlusOil.txt
echo '# 1' >> ../VPlusAllMinusNews.txt
echo '# 1' >> ../VPlusOil.txt
cat knowledge/oils.txt >> ../VPlusAllMinusNews.txt
cat knowledge/oils.txt >> ../VPlusOil.txt

echo >> ../VPlusAllMinusNews.txt
echo >> ../VPlusPDF.txt
echo '# 2' >> ../VPlusAllMinusNews.txt
echo '# 2' >> ../VPlusPDF.txt
cat knowledge/base_PDF.txt >> ../VPlusAllMinusNews.txt
cat knowledge/base_PDF.txt >> ../VPlusPDF.txt

echo >> ../VPlusAllMinusNews.txt
echo >> ../VPlusVideo.txt
echo '# 3' >> ../VPlusAllMinusNews.txt
echo '# 3' >> ../VPlusVideo.txt
cat knowledge/video_database_new.txt >> ../VPlusAllMinusNews.txt
cat knowledge/video_database_new.txt >> ../VPlusVideo.txt

echo >> ../VPlusAllMinusNews.txt
echo >> ../VPlusDialog.txt
echo '# 4' >> ../VPlusAllMinusNews.txt
echo '# 4' >> ../VPlusDialog.txt
cat knowledge/dialog_database.txt >> ../VPlusAllMinusNews.txt
cat knowledge/dialog_database.txt >> ../VPlusDialog.txt

echo >> ../VPlusNews.txt
echo '# 5' >> ../VPlusNews.txt
cat knowledge/press_news.txt >> ../VPlusNews.txt







