"""
Funkcja służy do pobierania danych do uczenia z pliku.
laduje dane do pamięci operacyjnej do dalszego przetwarzania przez kolejne częsci programu.
"""
import csv
import numpy

PATH_TO_FILE = "../data/car.data"


class Reader:
    data = []
    numpy_data = []
    isFetched = False

    def fetch_data(self):
        try:
            with open(PATH_TO_FILE, 'rt') as raw_data:
                reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
                self.data = list(reader)
                self.numpy_data = numpy.array(self.data)
                self.numpy_data = self.numpy_data.astype('str')
                raw_data.close()
            self.isFetched = True
        except IOError:
            print("Could not read file:", PATH_TO_FILE)

    def get_data(self):
        if self.isFetched == True:
            return self.data
        else:
            return []

    def get_numpy_data(self):
        if self.isFetched == True:
            return self.numpy_data
        else:
            return []