from sol_1 import solve_1
from sol_2 import solve_2

def test_1_data_1():
    assert solve_1([0,3,6,9,12,15])==18


def test_1_data_2():
    assert solve_1([1,3,6,10,15,21])==28

def test_1_data_3():
    assert solve_1([10,13,16,21,30,45])==68

def test_2_data_1():
    assert solve_2([0,3,6,9,12,15])==-3


def test_2_data_2():
    assert solve_2([1,3,6,10,15,21])==0

def test_2_data_3():
    assert solve_2([10,13,16,21,30,45])==5

