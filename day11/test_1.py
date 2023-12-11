from sol_1 import find_start
from sol_1 import sol_1

# from sol_2 import find_start

def test_1_find_start():
    assert find_start([['-', 'L', '|', 'F', '7'], ['7', 'S', '-', '7', '|'], ['L', '|', '7', '|', '|'], ['-', 'L', '-', 'J', '|'], ['L', '|', '-', 'J', 'F']])=={"position": [1,1], "direction": "F"}

def test_1_find_start_2():
    assert find_start([['.', '.', 'F', '7', '.'], ['.', 'F', 'J', '|', '.'], ['S', 'J', '.', 'L', '7'], ['|', 'F', '-', '-', 'J'], ['L', 'J', '.', '.', '.']])=={"position": [0,2], "direction": "F"}

def test_1_sol_1():
    assert sol_1("test1.txt")==8

def test_1_sol_1_2():
    assert sol_1("test2.txt")==4
