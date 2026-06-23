# F5 real-time webhook LIVE TEST — 20260623T210141Z. Intentional failure.
def add(a, b):
    return a - b  # BUG (intentional)


def test_add():
    assert add(2, 3) == 5
