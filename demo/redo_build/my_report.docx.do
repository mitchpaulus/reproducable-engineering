exec >&2

redo-ifchange my_report.md
pandoc --to docx -o "$3" my_report.md
