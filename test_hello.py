import pytest

from hello import greet


def test_greet_world():
    assert greet("world") == "Hello, world!"


def test_greet_named():
    assert greet("David") == "Hello, David!"


def test_greet_empty_string():
    assert greet("") == "Hello, !"


def test_greet_unicode():
    assert greet("世界") == "Hello, 世界!"


@pytest.mark.parametrize(
    "name,expected",
    [
        ("Alice", "Hello, Alice!"),
        ("Bob", "Hello, Bob!"),
        ("  ", "Hello,   !"),
    ],
)
def test_greet_parametrized(name: str, expected: str):
    assert greet(name) == expected
