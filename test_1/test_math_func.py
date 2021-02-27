# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 00:42:40 2020

@author: Rahul Sapireddy
"""

import math_func
import pytest
import sys

@pytest.mark.skipif(sys.version_info < (3, 3), reason="do not run number add test")
def test_add():
    assert math_func.add(7,3) == 10
    assert math_func.add(7) == 9
    print(math_func.add(7,3), "-------------------")

def test_product():
    assert math_func.product(5,5) == 25
    assert math_func.product(5) == 10

def test_add_strings():
    result = math_func.add("Hello", " World")
    assert result == "Hello World"
    assert type(result) is str
    assert "Heldlo" not in result

def test_product_strings():
    assert math_func.product("Hello ", 3) == "Hello Hello Hello "
    result = math_func.product("Hello ")
    assert result == "Hello Hello "
    assert type(result) is str
    assert "Hello" in result
    
