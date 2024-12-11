from src.main import add, sub


def test_add():
    assert add(2, 3) == 5
    assert add(99, 1) == 100


def test_sub():
    assert sub(2, 3) == -1
    assert sub(99, 1) == 98