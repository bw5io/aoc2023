from sol_1 import sol_1
# from sol_2 import sol_2
from sol_1 import assess_record

def test_1():
    assert sol_1("test1.txt") == 288

def test_2():
    assert sol_2("test1.txt") == 940200

def test_unit1():
    assert assess_record(7, 9) == 4

def test_unit2():
    assert assess_record(15, 40) == 8

def test_unit3():
    assert assess_record(30, 200) == 9
