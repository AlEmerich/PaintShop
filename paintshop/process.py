"""Package to answer to retrive set of colors to please every customers.
"""
import numpy as np

def is_satisfied(colorset, pref):
    """Return a tuple (boolean, num_color) if the customer's
    preference match with the specified colorset. If False, num_color
    is the color to change in the colorset."""
    num_m = -1

    for i in range(len(pref) // 2):
        num = int(pref[i*2]) - 1
        color = pref[i*2+1]
        if colorset[num] == color:
            return True, -1
        if color is 'M':
            num_m = num
    return False, num_m


def get_optimal_set(path):
    """Get the colorset who please every customer,
    or No solution exists if there is none.
    """
    with open(path, 'r') as f:
        contents = f.readlines()

    # Get the number of color
    num_of_color = int(contents[0].strip())

    # Initialize with gloss color, because we
    # want to minimize matte color
    result = ['G' for x in range(num_of_color)]

    # Two steps:
    # 1: The first pass is used to change the colorset, to please each consumer.
    # 2: The second pass is used to validate the result colorset. If someone is not
    #    pleased anymore, that means it is conflicted with another customers so there
    #    is no solution.
    # Note: The lines in the files must be sorted by length to make this algorithm
    #       works.
    for step in range(2):
        for lines in sorted(contents[1:], key=len):
            l_arr = lines.strip().split(" ")
            satisfied, num_c = is_satisfied(result, l_arr)
            if not satisfied:
                if step == 0:
                    result[num_c] = 'M'
                else:
                    return "No solution exists"

    return result
