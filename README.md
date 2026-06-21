# CI demo (intentionally broken)

This repository is intentionally broken for testing an automated CI-fix bot.

- `app/banner.py` imports `pyfiglet` and renders "CI DEMO" at import time.
- `requirements.txt` intentionally lists only `pytest` and omits `pyfiglet`.

When GitHub Actions runs the `CI` workflow it will install `pytest` only,
then run `pytest` which will fail during collection with:

```
ModuleNotFoundError: No module named 'pyfiglet'
```

The correct fix is to add `pyfiglet` to `requirements.txt`.
# final_test