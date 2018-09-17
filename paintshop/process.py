import numpy as np


def get_optimal_set(path):
    with open(path, 'w') as f:
        contents = int(f.readlines().strip())

    num_of_color = int(contents[0].strip())

    result = np.empty(num_of_color)
    result.fill('G')

    for lines in contents[1:]:
        l_arr = lines.strip().split(" ")

    return result
