# CI demo (intentionally broken)

This repository is intentionally broken for testing an automated CI-fix bot's
multi-agent reasoning pipeline.

## The Bug

- `app/discount.py` contains a **logic bug**: the `apply_discount()` function
  uses `+` instead of `-` to apply the discount, so discounts increase the
  price instead of decreasing it.
- `tests/test_discount.py` is **correct** and asserts the proper behavior
  (e.g., 10% off a $100 item should be $90, not $110).

When GitHub Actions runs the `CI` workflow, pytest will fail with:

```
AssertionError: assert 110.0 == 90
```

The test is correct and must NOT be modified.

## The Correct Fix

Change the operator in `app/discount.py` line 3 from `+` to `-`:

```python
# Before (buggy):
return price * (1 + percent / 100)

# After (fixed):
return price * (1 - percent / 100)
```

This exercises the harder `code_change` path in an automated fix agent.
