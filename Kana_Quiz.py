import random

p=[]
for i in range(46):
	p.append(random.randint(0,2))

r=['0a0A a','0i0I i','0u0U u','0e0E e','0o0O o','KaKAka','KiKIki','KuKUku','KeKEke','KoKOko','SaSAsa','SiSIsI','SuSUsu','SeSEse','SoSOso','TaTAta','TiTItI','TuTUtU','TeTEte','ToTOto','NaNAna','NiNIni','NuNUnu','NeNEne','NoNOno','HaHAha','HiHIhi','FuFUfu','HeHEhe','HoHOho','MaMAma','MiMImi','MuMUmu','MeMEme','MoMOmo','YaYAya','YuYUyu','YoYOyo','RaRAra','RiRIri','RuRUru','ReREre','RoROro','WaWAwa','1o1Oo*','0n0N n']
random.shuffle(r)

print '\documentclass[UTF8]{ctexart}'
print '\usepackage{multicol}'
print '\pagestyle{empty}'
print '\\begin{document}'
print '\\begin{multicols}{2}'
print '\\begin{center}'
print '\\begin{tabular}{rccc}'

for i in range(23):
	if (p[i]==0):
		print i+1,'&'+r[i][0:2]+'&\\framebox[6mm]{\\rule{0pt}{4mm}}&\\framebox[6mm]{\\rule{0pt}{4mm}}\\\\'
	else:
		if (p[i]==1):
			print i+1,'&\\framebox[6mm]{\\rule{0pt}{4mm}}&'+r[i][2:4]+'&\\framebox[6mm]{\\rule{0pt}{4mm}}\\\\'
		else:
			print i+1,'&\\framebox[6mm]{\\rule{0pt}{4mm}}&\\framebox[6mm]{\\rule{0pt}{4mm}}&'+r[i][4:6]+'\\\\'

print '\end{tabular}'
print '\end{center}'
print '\\begin{center}'
print '\\begin{tabular}{rccc}'

for i in range(23,46):
	if (p[i]==0):
		print i+1,'&'+r[i][0:2]+'&\\framebox[6mm]{\\rule{0pt}{4mm}}&\\framebox[6mm]{\\rule{0pt}{4mm}}\\\\'
	else:
		if (p[i]==1):
			print i+1,'&\\framebox[6mm]{\\rule{0pt}{4mm}}&'+r[i][2:4]+'&\\framebox[6mm]{\\rule{0pt}{4mm}}\\\\'
		else:
			print i+1,'&\\framebox[6mm]{\\rule{0pt}{4mm}}&\\framebox[6mm]{\\rule{0pt}{4mm}}&'+r[i][4:6]+'\\\\'

print '\end{tabular}'
print '\end{center}'
print '\end{multicols}'
print '\\newpage'
print '\\begin{multicols}{2}'
print '\\begin{center}'
print '\\begin{tabular}{rccc}'

for i in range(23):
	if (p[i]==0):
		print i+1,'&'+r[i][0:2]+'&\\framebox[6mm]{\\rule{0pt}{4mm}'+r[i][2:4]+'}&\\framebox[6mm]{\\rule{0pt}{4mm}'+r[i][4:6]+'}\\\\'
	else:
		if (p[i]==1):
			print i+1,'&\\framebox[6mm]{\\rule{0pt}{4mm}'+r[i][0:2]+'}&'+r[i][2:4]+'&\\framebox[6mm]{\\rule{0pt}{4mm}'+r[i][4:6]+'}\\\\'
		else:
			print i+1,'&\\framebox[6mm]{\\rule{0pt}{4mm}'+r[i][0:2]+'}&\\framebox[6mm]{\\rule{0pt}{4mm}'+r[i][2:4]+'}&'+r[i][4:6]+'\\\\'

print '\end{tabular}'
print '\end{center}'
print '\\begin{center}'
print '\\begin{tabular}{rccc}'

for i in range(23,46):
	if (p[i]==0):
		print i+1,'&'+r[i][0:2]+'&\\framebox[6mm]{\\rule{0pt}{4mm}'+r[i][2:4]+'}&\\framebox[6mm]{\\rule{0pt}{4mm}'+r[i][4:6]+'}\\\\'
	else:
		if (p[i]==1):
			print i+1,'&\\framebox[6mm]{\\rule{0pt}{4mm}'+r[i][0:2]+'}&'+r[i][2:4]+'&\\framebox[6mm]{\\rule{0pt}{4mm}'+r[i][4:6]+'}\\\\'
		else:
			print i+1,'&\\framebox[6mm]{\\rule{0pt}{4mm}'+r[i][0:2]+'}&\\framebox[6mm]{\\rule{0pt}{4mm}'+r[i][2:4]+'}&'+r[i][4:6]+'\\\\'

print '\end{tabular}'
print '\end{center}'
print '\end{multicols}'
print '\end{document}'
