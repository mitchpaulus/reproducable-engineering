
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

def task_report():
    return {
            "file_dep" : [ "eplusout.png", "my_report.tex" ],
            "actions" : [ ["lualatex", "--output-directory", "latex_build", "my_report.tex"] ],
            "targets" : [ "my_report.pdf" ],
            "doc": "Compile our report"
       }


def task_py_params_list():
    def print_a_list(list):
        for item in list:
            print(item)
    return {'actions':[(print_a_list,)],
            'params':[{'name':'list',
                       'short':'l',
                       'long': 'list',
                       'type': list,
                       'default': [],
                       'help': 'Collect a list with multiple -l flags'}],
            'verbosity':2,
            }

