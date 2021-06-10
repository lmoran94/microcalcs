import json
import json5
import sys
import csv
import numpy as np
from collections import OrderedDict

total_weight=0.0
with open("input/weightings.csv","r") as weights_file:
    csv_reader = csv.reader(weights_file, delimiter=',')
    next(csv_reader)
    for weight in csv_reader:
        weight = float(weight[0])
        total_weight += weight

with open("input/mcrt_microcalcraman.json5","r") as jsonFile:
    data = json5.load(jsonFile)

#(json5.parse(data))
outerLight = data["light"]
#print("outerLight", outerLight)
innerLight = outerLight["Here"]
innerLight["power"] = float(total_weight)
#print("outerlightpower", outerLight["power"])
#print(innerLight)
#innerLight = float(sys.argv[1])
#print(innerLight)
#print(outerLight)
#print("data: ", data)
with open("input/mcrt_microcalcraman.json5", "w") as jsonFile:
    json5.dump(data, jsonFile)
