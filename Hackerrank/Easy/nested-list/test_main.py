import main
import pytest


def test_1():
    output = main.main(['Harry', 'Berry', 'Tina', 'Akriti', 'Harsh'], [37.21, 37.21, 37.2, 41, 39])
    assert output == ['Berry', 'Harry']


def test_2():
    output = main.main(['Tina', 'Akriti', 'Harsh'], [37.2, 41, 39])
    assert output == ['Harsh']


def test_3():
    output = main.main(['Akriti', 'Harsh', 'Berry'], [41, 39, 222])
    assert output == ['Akriti']
