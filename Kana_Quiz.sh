python Kana_Quiz.py >tmp.tex
vi -s Kana_replace tmp.tex
latex -output-format=pdf tmp.tex
mv tmp.pdf Kana_Quiz.pdf
rm tmp*
