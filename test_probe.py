# E2E loop probe — added 2026-06-23 for pre-go-live verification.
# Intentional bug so the Copilot can detect, root-cause, and fix it.

def multiply(a, b):
    return a + b  # BUG: should be a * b


def test_multiply():
    assert multiply(3, 4) == 12
