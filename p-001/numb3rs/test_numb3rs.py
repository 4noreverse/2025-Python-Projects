import re
import sys
from numb3rs import validate



def test_first_byte():
    bad_ip = '192.555.421.362'
    assert validate(bad_ip) == False


def test_five_byte():
    fdhfmf = '192.192.192.192.192'
    assert validate(fdhfmf) == False
