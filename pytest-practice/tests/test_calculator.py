

from calculator import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 4) == -4

