import main
import pytest


def test_1():
    output = main.can_pill_up(6, [4, 3, 2, 1, 3, 4])
    assert output == 'Yes'


def test_2():
    output = main.can_pill_up(4, [1, 3, 3, 4])
    assert output == 'Yes'


def test_3():
    output = main.can_pill_up(12, [4, 3, 2, 1, 3, 4, 4, 3, 2, 1, 3, 4])
    assert output == 'No'
