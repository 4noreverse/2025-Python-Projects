import re
import sys
from working import convert


def test_work_one():
    s = '000:0 AM to 12:30 PM'
    try:
        convert(s)
        assert False
    except ValueError:
        pass

def test_work_two():
    s = "6:00 AM to 4:00 PM"
    answer = "06:00 to 16:00"
    assert convert(s) == answer

def test_work_tree():
    s = "4:30 PM to 6 PM"
    answer = "16:30 to 18:00"
    assert convert(s) == answer

def test_work_four():
    s = "4:30 PM 6PM"
    try:
        convert(s)
        assert False
    except ValueError:
        pass
def test_work_five():
    s = "0:30 AM to 5:00 PM"
    try:
        convert(s)
        assert False
    except ValueError:
        pass


