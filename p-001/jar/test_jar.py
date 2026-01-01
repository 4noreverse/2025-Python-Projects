from jar import Jar

def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    assert str(jar) == ''
    jar.deposit(2)
    assert str(jar) == '🍪🍪'
    jar.deposit(7)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪🍪🍪🍪'

def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3
    try:
        jar.deposit(20)
    except ValueError:
        pass
    else:
        assert False



def test_withdraw():
    jar = Jar(12)
    jar.deposit(12)
    assert jar.size == 12
    jar.withdraw(2)
    assert jar.size == 10
    try:
        jar.withdraw(20)
    except ValueError:
        pass
    else:
        assert False





