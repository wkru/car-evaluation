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

s1 = stump.Stump('maint')
s2 = stump.Stump('buying')
s3 = stump.Stump('doors')
s4 = stump.Stump('persons')
s5 = stump.Stump('lug_boot')
s6 = stump.Stump('safety')
s1.learn(data)
s2.learn(data)
s3.learn(data)
s4.learn(data)
s5.learn(data)
s6.learn(data)
