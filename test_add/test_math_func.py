# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 00:29:35 2020

@author: Rahul Sapireddy
"""

import math_func
import pytest

@pytest.mark.parametrize('x, y, result', 
                         [
                                (7, 3, 10),
                                ("Hello", " World", "Hello World"),
                                (10.5, 25.5, 36)
                       ])

def test_add(x, y, result):
    assert math_func.add(x,y) == result
    

"""
def test_add():
    assert math_func.add(7,3) == 10
    result = math_func.add("Hello", " World")
    assert result == "Hello World"
    result = math_func.add(10.5,25.5)
    assert result == 36
"""


"""   
def test_add():
    assert math_func.add(7,3) == 10
    
def test_add_strings():
    result = math_func.add("Hello", " World")
    assert result == "Hello World"
    
def test_add_float():
    result = math_func.add(10.5,25.5)
    assert result == 36
"""
