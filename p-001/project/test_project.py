import os
import json
import requests
from project import load, save, port_value
test_port = 'test_port.json'

def test_load():
    test_data = {
        'sol': 2.4,
        'doge': 3000,
        'link': 500.9
    }
    with open(test_port,'w') as file:
        json.dump(test_data, file)
    port = load(test_port)
    assert port == test_data

    if os.path.exists(test_port):
        os.remove(test_port)

def test_save():
    test_data = {
        'sol': 2.4,
        'doge': 3000,
        'link': 500.9
    }
    save(test_data, test_port)

    with open(test_port, 'r') as file:
        x = json.load(file)

    assert x == test_data

    if os.path.exists(test_port):
        os.remove(test_port)

def test_port_value():
    test_data = {
        'sol': 2.4,
        'doge': 3000,
        'link': 500.9
    }
    def test_price(tick):
        return {'sol': 50, 'doge': 25, 'link': 700}[tick]
    total, indiv = port_value(test_data, test_price)
    assert total == 425750.00
    assert indiv['sol'] == 120.00
    assert indiv['doge'] == 75000.00
    assert indiv['link'] == 350630.00



