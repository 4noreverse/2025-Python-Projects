from um import count
import re
import sys

def test_one():
    assert count('yummy') == 0
def test_two():
    assert count('ummmmmmmmm') == 0
def test_three():
    assert count('um, hello um hi') == 2
def test_four():
    assert count('UM um um?') == 3

