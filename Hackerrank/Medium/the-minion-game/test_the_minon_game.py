import main
import pytest


def test_1():
    output = main.merge_the_tools('AABCAAADA', 3)
    assert output == ['AB', 'CA', 'AD']


def test_2():
    output = main.merge_the_tools('ABCDEF', 3)
    assert output == ['ABC', 'DEF']


def test_3():
    output = main.merge_the_tools('AABCAAAD', 4)
    assert output == ['ABC', 'AD']
