exec >&2
energyplus -r -d ../eplus_output/ ../CoolingTower.idf
cp ../eplus_output/$1 $3
