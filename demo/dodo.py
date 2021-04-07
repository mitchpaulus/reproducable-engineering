def task_energyplus():
    return {
            "file_dep": [ "CoolingTower.idf" ],
            "actions": [ ["energyplus.exe", "-r", "-d", "eplus_output", "CoolingTower.idf"] ],
            "targets": [ "eplus_output/eplusout.csv" ],
            "doc": "Run our EnergyPlus model"
    }

def task_png_image():
    return {
                "file_dep" : [ "eplus_output/eplusout.csv" ],
                "actions" : [ ["pipenv", "run", "python", "make_fig.py", "eplus_output/eplusout.csv", "eplusout.png" ]],
                "targets": [ "eplusout.png" ]
            }
