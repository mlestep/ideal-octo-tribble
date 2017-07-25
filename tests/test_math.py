"""
Testing for the math.py module
"""

import octo_tribble as ot
import pytest

def test_add():
    assert ot.math.add(5, 2) == 7
    assert ot.math.add(2, 5) == 7
