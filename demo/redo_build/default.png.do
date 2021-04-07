redo-ifchange $2.csv make_fig.py
pipenv run python make_fig.py $2.csv "$3" >&2
