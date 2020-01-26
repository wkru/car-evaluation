# Load CSV (using python)
import csv
import numpy
import stump
import names as n
import random as r

raw_data = open("../data/car.data", 'rt')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('str')

s = []

for i in range (0, 1000):
    a= n.col_names2[r.randint(0,5)];
    #print(a)
    s.append(stump.Stump(a))

for st in s:
    st.learn(r.sample(x,100))
good_counter = 0
for row in range(0, int(data.size / 7)):
    results = []
    for st in s:
        results.append(st.evaluate(data[row]))
    c = numpy.bincount(numpy.array(results)).argmax()
    d = n.quality_values[data[row][6]]
    if c == d:
        good_counter += 1
print(good_counter)

