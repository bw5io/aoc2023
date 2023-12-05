from sol_1 import sol_1
from sol_2 import sol_2
from sol_2 import run_rules

def test_1():
    assert sol_1("test1.txt") == 35

def test_2():
    assert sol_2("test1.txt") == 46

def test_unit1():
    assert run_rules([[5,30]], [[32,2,16]]) == [[35, 47], [18, 30]]

def test_unit2():
    assert run_rules([[0,1]], [[32,2,16]]) == [[0,1]]

def test_unit3():
    assert run_rules([[4,8]], [[32,2,16]]) == [[34,38]]

def test_unit4():
    assert run_rules([[1,30]], [[32,2,16]]) == [[32,47],[1,1],[18,30]]