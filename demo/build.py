import subprocess
import csv
import matplotlib.pyplot as plt

subprocess.run(["energyplus", "-r", "-d", "eplus_output/", "CoolingTower.idf"])

xy_pairs = []

with open("eplus_output/eplusout.csv") as eplus_data:
    data = list(csv.reader(eplus_data))
    for row in data[1:]:
        temp_celcius = float(row[1])
        if temp_celcius > 0:
            temp_fahrenheit = temp_celcius * (9/5) + 32
            xy_pairs.append(float(temp_fahrenheit))

fig, ax = plt.subplots()
ax.plot(xy_pairs)  # Matplotlib plot.

fig.savefig('out.png')

subprocess.run(["lualatex", "my_report.tex"])
