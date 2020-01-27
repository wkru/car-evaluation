"""
Funkcja dokonująca walidacji krzyżowej modelu aproksymacyjnego.
"""

import names as n
import random as r


def cross_validate(k, model, data):
    r.shuffle(data)
    num_of_subsets = k
    size_of_subset = n.NUM_OF_ROWS/k
    total_errors_count = 0

    for subset_index in range(0, num_of_subsets):
        starting_point = int(subset_index*size_of_subset)
        ending_point = int((subset_index+1)*size_of_subset)

        if ending_point >= n.NUM_OF_ROWS:
            ending_point = n.NUM_OF_ROWS - 1

        data_to_learn_from = data[0:starting_point]+data[ending_point:n.NUM_OF_ROWS-1]

        model.fit_forest_to_data(n.SIZE_OF_SAMPLE, data_to_learn_from)
        subset = data[starting_point:ending_point]

        errors_in_sample_count = model.evaluate_data_set(subset)
        total_errors_count += errors_in_sample_count
        #print("Wskaźnik jakości dla próbki",subset_index,":", errors_in_sample_count)

    average_loss = total_errors_count / num_of_subsets
    model.fit_forest_to_data(n.SIZE_OF_SAMPLE,data)
    print("Wskaźnik jakości dla całej próbki:", average_loss)
    print("Poprawnie dopasowano:", "%.2f" % (100-average_loss/size_of_subset*100),"% próbek")
    return 100-average_loss/size_of_subset*100