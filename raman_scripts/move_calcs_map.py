import json
import sys
import csv
import numpy as np
from collections import OrderedDict


new_rows = []
with open("input/og_sphere_calc.csv","r") as points_file:
    csv_reader = csv.reader(points_file, delimiter=',')
    for row in csv_reader:
        row = [float(i) for i in row]
        row[1] += float(sys.argv[2])
        row[2] += float(sys.argv[1])
        new_rows.append(row)

print("POINTS: ", new_rows)

#outerTrans = data["trans"]
#innerTrans = outerTrans["trans"]
#print(innerTrans)
#innerTrans[0] = np.float(sys.argv[1])
#print(innerTrans)
#print(outerTrans)
#print("data: ", data)



with open("input/sphere_calc.csv", "w") as points_file:
    csv_writer = csv.writer(points_file, delimiter=',')
    csv_writer.writerows(new_rows)
