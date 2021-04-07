exec >&2

redo-ifchange CoolingTower.idf
energyplus.exe -r -d ../eplus_output/ CoolingTower.idf
cp ../eplus_output/$1 $3
