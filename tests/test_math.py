"""
Testing for the math.py module
"""

import octo_tribble as ot
import pytest

def test_add():
    assert ot.math.add(5, 2) == 7
    assert ot.math.add(2, 5) == 7

def test_mult():
    assert ot.math.mult(1, 3) == 3
    assert ot.math.mult(3, 1) == 3
    assert ot.math.mult(2, 5) == 10
    assert ot.math.mult(5, 2) == 10

#def test_awesome():


