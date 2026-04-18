# hello-world

The quintessential "Hello, world!" program, in Python, with tests.

## Run

```sh
python3 hello.py
```

Expected output:

```
Hello, world!
```

## Test

```sh
pip install -r requirements-dev.txt
pytest
```

## CI

Every push and pull request runs the test suite and then `hello.py` via
GitHub Actions — see the [Actions tab](../../actions) for output.
