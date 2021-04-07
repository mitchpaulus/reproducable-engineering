exec >&2

redo-ifchange my_report.tex eplusout.png
lualatex --output-directory='latex_build' my_report.tex
cp latex_build/my_report.pdf "$3"
