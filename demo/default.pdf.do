exec >&2
redo-ifchange "$2.tex" eplusout.png
lualatex --output-directory='redo_build' "$2".tex
cp redo_build/"$2".pdf "$3"
