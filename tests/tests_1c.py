"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_arrays(): 
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert max_subarray_sum([0,1,-1]) == 1
    assert max_subarray_sum([-2,3,-3,7]) == 7

if __name__ == "__main__":
    pytest.main()