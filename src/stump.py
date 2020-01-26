import names as n

class Stump:
    decision_dictionary = []
    feature = 0

    def __init__(self, feature):
        self.feature = n.col_names[feature]

    def learn(self, dataset):
        counter = [[0] * len(n.col_values[self.feature]) for i in range(len(n.col_values[self.feature]))]
        for row in range(0, int(dataset.size/7)-1):
            #index of feature value from dataset
            i = n.col_values[self.feature][dataset[row][self.feature]]
            #index of quality value
            j = n.quality_values[dataset[row][6]]
            counter[i][j] += 1
        print(counter)
