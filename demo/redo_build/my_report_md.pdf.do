exec >&2

redo-ifchange my_report.md eplusout.png
pandoc --to pdf -o $3 my_report.md
