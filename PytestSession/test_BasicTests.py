import pytest


@pytest.mark.test
def test_Login():
    a = 10
    b = 5
    print("This is marked one")
    assert a != b, "test is failed one"


@pytest.mark.test
def test_Login2():
    a = 10
    b = 5
    print("This is marked one")
    assert a != b, "test is failed two"


def test_Login3():
    a = 10
    b = 5
    assert a != b, "test is failed"


def test_Login4():
    a = 10
    b = 5
    assert a != b, "test is failed"


def test_Login5():
    a = 10
    b = 5
    assert a != b, "test is failed"
