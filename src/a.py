# Load CSV (using python)
import csv
import numpy
import stump

raw_data = open("../data/car.data", 'rt')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('str')
print(data.shape)

# create wyrżnięty forest

s = stump.Stump('maint')
s.learn(data)
