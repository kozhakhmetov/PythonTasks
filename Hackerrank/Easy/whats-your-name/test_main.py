import main
import pytest


def test_1():
    output = main.main('Ross', 'Taylor')
    assert output == 'Hello Ross Taylor! You just delved into python.'


def test_2():
    output = main.main('Adilkhan', 'Kozhakhmetov')
    assert output == 'Hello Adilkhan Kozhakhmetov! You just delved into python.'


def test_3():
    output = main.main('someone', 'someoneov')
    assert output == 'Hello someone someoneov! You just delved into python.'
