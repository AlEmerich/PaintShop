# Sample Test passing with nose and pytest
from paintshop.process import get_optimal_set

def test_no_solution():
    colorset = get_optimal_set("no_solution.txt")
    assert colorset == "No solution exists", \
        "A solution is found where there is none: " + str(colorset)

def test_first_example():
    colorset = get_optimal_set("first.txt")
    assert colorset == ['G', 'G', 'G', 'G', 'M'], \
        "Wrong solution: " + str(colorset)

def test_second_example():
    colorset = get_optimal_set("second.txt")
    assert colorset == ['G','M','G','M','G'], \
        "Wrong solution: " + str(colorset)

def test_third_example():
    colorset = get_optimal_set("third.txt")
    assert colorset == ['M', 'M'], \
        "Wrong solution: " + str(colorset)
