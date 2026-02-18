"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_found(): 
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([80, 90, 1], 81) == [0, 2]

def test_not_found(): 
    assert two_sum([0, 1], 10) == []
    assert two_sum([80, 90, 1], 70) == []

if __name__ == "__main__":
    pytest.main()