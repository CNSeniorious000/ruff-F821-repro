# Ruff Lint F821 reproduction

```sh
> ruff check

1 file left unchanged
hello.py:9:11: F821 Undefined name `anext`. Consider specifying `requires-python = ">= 3.10"` or `tool.ruff.target-version = "py310"` in your `pyproject.toml` file.
|
8 | async def main():
9 | print(anext(g()))
| ^^^^^ F821
|

Found 1 error.
```
