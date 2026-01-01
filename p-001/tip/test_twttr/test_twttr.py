from twttr import shorten

def test_twttr():
    shorten('ethandalton') == 'thndltn'

def test_no():
    assert shorten('ethandalton') != 'ethandalton'

def test_upper():
    assert shorten('ethandalton') != 'THNDLTN'

def test_num():
    assert shorten('CS50') == 'CS50'

def test_punc():
    assert shorten('whats your name?') == 'whts yr nm?'

def test_lower():
    assert shorten('YO') == 'Y'


