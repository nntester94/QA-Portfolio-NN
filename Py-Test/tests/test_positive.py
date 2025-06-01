import pytest
from positive import is_positive 

@pytest.mark.parametrize("input, expected", [
    (2,True),
    (788,True),
    (-4,False),
    (0,False)

])
def test_is_positive(input, expected):
    assert is_positive(input) == expected