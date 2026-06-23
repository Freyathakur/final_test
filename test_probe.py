# F5 real-time webhook probe — 2026-06-23. Intentional failure.
def add(a, b):
    return a - b  # BUG


def test_add():
    assert add(2, 3) == 5
