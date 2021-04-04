.PHONY : all
all : my_report.pdf

my_report.pdf : my_report.tex eplusout.png
	lualatex $<

eplus_output/eplusout.csv : CoolingTower.idf
	energyplus -r -d eplus_output/ $<

%.png : eplus_output/%.csv make_fig.py
	pipenv run python make_fig.py $<

.PHONY : clean
clean :
	rm -rf eplus_output/*
	rm out.png
