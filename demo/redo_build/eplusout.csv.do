exec >&2 # Just needed to prevent standard output from EnergyPlus polluting the output.

redo-ifchange CoolingTower.idf
energyplus.exe -r -d eplus_output CoolingTower.idf
cp eplus_output/eplusout.csv $3
