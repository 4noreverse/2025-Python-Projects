from plates import is_valid

def test_valid():
    assert is_valid('yoo34') == True

def test_long():
    assert is_valid('yooo341') == False

def test_one():
    assert is_valid('2343') == False

def test_two():
    assert is_valid('34yy') == False

def test_punc():
    assert is_valid('yo?24,') == False

def test_numafter():
    assert is_valid('hl345yo') == False

def test_numplace():
    assert is_valid('yy54y') == False

def test_zero():
    assert is_valid('cs05') == False
