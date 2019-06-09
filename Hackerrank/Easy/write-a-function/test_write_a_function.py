import main
import pytest


def test_1():
    output = main.is_leap(2000)
    assert output is True


def test_2():
    output = main.is_leap(1997)
    assert output is False


def test_3():
    output = main.is_leap(1234)
    assert output is False
