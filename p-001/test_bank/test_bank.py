from bank import value

def test_value():
    assert value('yo') == 100
def test_one():
    assert value('hey') == 20
def test_two():
    assert value('hello') == 0
def test_three():
    assert value('HEY') == 20
def test_four():
    assert value('HELLO') == 0
def test_five():
    assert value('h') == 20
def test_six():
    assert value('hello, Newman') == 0
