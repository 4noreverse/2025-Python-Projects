from seasons import jork
import seasons
from datetime import date
import pytest

def test_jork_valid_date():
    dob = date(1998, 1, 19)
    result = jork(dob)
    assert isinstance(result, str)
    assert len(result) > 0
    assert any(word in result.lower() for word in ["million", "thousand", "zero", "one"])

def test_two():
    today = date.today()
    result = jork(today)
    assert isinstance(result, str)
    assert "zero" in result.lower()
