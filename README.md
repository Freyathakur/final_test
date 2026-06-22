# CI demo (intentionally broken)

This repository is intentionally broken for testing an automated CI-fix bot's
multi-agent pipeline.

## The Bug

- `discount.py` contains a **logic bug**: the `apply_discount()` function
  uses `+` instead of `-` to apply the discount, so discounts increase the
  price instead of decreasing it.
- `test_discount.py` is **correct** and asserts the proper behavior
  (e.g., 10% off a $100 item should be $90, not $110).

When GitHub Actions runs the `CI` workflow, pytest will fail with an
AssertionError:

```
AssertionError: assert 110.0 == 90
```

The test is correct and must NOT be modified.

## The Correct Fix

Change the operator in `discount.py` line 3 from `+` to `-`:

```python
# Before (buggy):
return price * (1 + percent / 100)

# After (fixed):
return price * (1 - percent / 100)
```

This exercises the `code_change` path in an automated fix agent.
