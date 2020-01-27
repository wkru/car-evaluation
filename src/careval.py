import forest
import names as n
import datareader as dr
import validate
from datetime import datetime

reader = dr.Reader()
reader.fetch_data()

numpy_data = reader.get_numpy_data()
data = reader.get_data()

if numpy_data.__sizeof__() == 0:
    print("Nie udało się pobrać danych")
    exit(1)
if data == []:
    print("Nie udało się pobrać danych")
    exit(1)

forest = forest.Forest(n.NUMBER_OF_STUMPS)

before = datetime.now()
forest.fit_forest_to_data(n.SIZE_OF_SAMPLE, data)
after = datetime.now()
diff = after - before
print("Czas dostosowania lasu dla całej próbki danych:", "%.3f" % (diff.total_seconds()*1000),'ms')

mean = 0
before = datetime.now()
mean += validate.cross_validate(5, forest, data)
mean += validate.cross_validate(5, forest, data)
mean += validate.cross_validate(5, forest, data)
mean += validate.cross_validate(5, forest, data)
mean += validate.cross_validate(5, forest, data)
after = datetime.now()
diff = after - before
print("czas:", "%.3f" % (diff.total_seconds()/5),'s')
print("średnia:", "%.2f" %(mean/5))

exit(0)