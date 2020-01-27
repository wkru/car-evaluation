col_names = {'buying': 0, 'maint': 1, 'doors': 2, 'persons': 3, 'lug_boot': 4, 'safety': 5}
col_names2 = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety']
col_values = [
     {'vhigh': 0, 'high': 1, 'med': 2, 'low': 3},
     {'vhigh': 0, 'high': 1, 'med': 2, 'low': 3},
     {'2': 0, '3': 1, '4': 2, '5more': 3},
     {'2': 0, '4': 1, 'more': 2},
     {'small': 0, 'med': 1, 'big': 2},
     {'low': 0, 'med': 1, 'high': 2}
]

quality_values = {'unacc': 0, 'acc': 1, 'good': 2, 'vgood': 3}
quality_numbers = [1210, 384, 69, 65]

FEATURES_NUMBER = 3
NUMBER_OF_STUMPS = 1000
SIZE_OF_SAMPLE = 20
NUM_OF_ROWS = 1728
TEST_DATA_PERCENTAGE = 0.2
INDEX_OF_Y = 6