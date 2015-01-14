python Kana_Quiz.py >tmp.tex
vi -s Kana_replace tmp.tex
xelatex tmp.tex
mv tmp.pdf Kana_Quiz.pdf
rm tmp*
