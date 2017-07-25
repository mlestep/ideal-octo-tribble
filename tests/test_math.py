"""
Testing for the math.py module
"""

import octo_tribble as ot
import pytest

def test_add():
    assert ot.math.add(5, 2) == 7
    assert ot.math.add(2, 5) == 7

testdata = [
    (2, 5, 10),
    (1, 2, 2),
    (11, 9, 99),
    (11, 0, 0),
    (0, 0, 0),
]

@pytest.mark.parametrize("a,b,expected", testdata)
def test_mult(a, b, expected):
    assert ot.math.mult(a, b) == expected
    assert ot.math.mult(b, a) == expected

testdata2 = [
    (1, 2, 95),
    (0, 0, 42),
    (-5, 10, 30167),
    (2, 2, 110),
    (3, 7, 7290),
]

@pytest.mark.parametrize("a,b,expected", testdata2)
def test_awesome(a, b, expected):
    assert ot.submodule.more_functs.awesome(a, b) == expected


