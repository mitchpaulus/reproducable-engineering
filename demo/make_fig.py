import csv
import matplotlib.pyplot as plt
import sys

input_filepath = sys.argv[1]
output_filepath = sys.argv[2]

xy_pairs = []

with open(input_filepath) as eplus_data:
    data = list(csv.reader(eplus_data))
    for row in data[1:]:
        temp_celcius = float(row[1])
        if temp_celcius > 0:
            temp_fahrenheit = temp_celcius * (9/5) + 32
            xy_pairs.append(float(temp_fahrenheit))

fig, ax = plt.subplots()
ax.plot(xy_pairs)  # Matplotlib plot.

fig.savefig(output_filepath, format='png')
