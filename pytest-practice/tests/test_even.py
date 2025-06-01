
import pytest
from even import is_even

@pytest.mark.parametrize("input, expected", [
    (2,True),
    (1,False),
    (0,True),
    (-5,False),
    (-4,True)
])
def test_is_even(input, expected):
    assert is_even(input) == expected