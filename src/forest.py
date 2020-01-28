"""
Klasa przechowująca model lasu losowego.

Tworzy i inicjalizuje pieńki decyzyjne oraz wywołuje metodę ich uczenia.
"""

import stump
import random as r
import names as n
import numpy

class Forest:
    stumps = []

    def __init__(self, number_of_stumps):

        for i in range(0, number_of_stumps):
            features = []
            for i in range(0, n.FEATURES_NUMBER):
                number_of_feature = r.randint(0, 5)
                features.append(number_of_feature)
            to_add = stump.Stump(features)
            self.stumps.append(to_add)

    def fit_forest_to_data(self, size_of_sample, data):

        for st in self.stumps:
            sample_of_data = r.sample(data, size_of_sample)
            st.learn(sample_of_data)

    def evaluate_data(self, data_row):
        results = []
        for st in self.stumps:
            result = st.evaluate(data_row)
            results.append(result)
        result = numpy.bincount(numpy.array(results)).argmax()
        return result

    def evaluate_data_set(self, data_rows_with_check, confusion_matrix):
        error_count = 0
        for row in data_rows_with_check:
            result = self.evaluate_data(row)
            if result != n.quality_values[row[n.INDEX_OF_Y]]:
                error_count += 1
                i = result
                j = n.quality_values[row[n.INDEX_OF_Y]]
                confusion_matrix[i][j] += 1
        return error_count
