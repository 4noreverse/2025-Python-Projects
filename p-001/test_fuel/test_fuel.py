from fuel import convert, gauge

def test_one():
    assert convert('3/4') == 75
def test_two():
    try:
        convert('1/0')
        assert False
    except ZeroDivisionError:
        assert True
def test_three():
    try:
        convert('2/1')
        assert False
    except ValueError:
        assert True
def test_neg():
    try:
        convert('-2/4')
        assert False
    except ValueError:
        assert True
def test_negother():
    try:
        convert('-4/2')
        assert False
    except ValueError:
        assert True

def test_four():
    assert gauge(1) == 'E'
def test_five():
    assert gauge(0) == 'E'
def test_six():
    assert gauge(50) == '50%'
def test_seven():
    assert gauge(99) == 'F'
def test_eight():
    assert gauge(100) == 'F'

