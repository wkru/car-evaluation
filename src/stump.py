import names as n
import sys
import math
import numpy as np

class Stump:

    def __init__(self, features):
        self.decision_dictionary = []
        self.features = features
        self.feature = -1

    def learn(self, dataset):
        self.decision_dictionary = []
        self.feature = -1
        counters = []
        for it in range(0, n.FEATURES_NUMBER):
            counters.append ([[0] * 4 for i in range(len(n.col_values[self.features[it]]))])
            for row in range(0, int(len(dataset))):
                # index of feature value from dataset
                i = n.col_values[self.features[it]][dataset[row][self.features[it]]]
                # index of quality value
                j = n.quality_values[dataset[row][6]]
                counters[it][i][j] += 1
        counter = counters[self.chooseBestFeature(counters)]
        for row in range(0, len(counter)):
            for col in range(0, len(counter[row])):
                counter[row][col] /= n.quality_numbers[col]
        index = len(n.col_values[self.feature])
        for feature in range(0, index ):
                maxv = counter[feature].index(max(counter[feature]))
                self.decision_dictionary.append(maxv)

    def evaluate(self, row):
        feature_value = row[self.feature]
        feature_value_index = n.col_values[self.feature][feature_value]
        return self.decision_dictionary[feature_value_index]

    def chooseBestFeature(self, counters):
        min_entropy = sys.maxsize
        num_of_counter = -1
        for i in range(0, n.FEATURES_NUMBER):
            avg_entropy = 0
            sum_of_array = np.sum(np.array(counters[i]))
            for k in range(0, len(n.col_values[self.features[i]])):
                entropy_in_row = 0
                sum_of_row = np.sum(np.array(counters[i][k]))
                if sum_of_row == 0:
                    continue
                for j in range(0, 4):
                    a = counters[i][k][j]/sum_of_row
                    if a != 0:
                        entropy_in_row -= a*math.log(a)
                avg_entropy += entropy_in_row*sum_of_row/sum_of_array
            if avg_entropy < min_entropy:
                min_entropy = avg_entropy
                self.feature = self.features[i]
                num_of_counter = i
        return num_of_counter
