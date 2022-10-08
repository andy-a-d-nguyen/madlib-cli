# Lab: 03 - Errors, Files, and Packaging 

## Madlib CLI

### Author: Andy Nguyen

### Setup

Make sure you are in the repo's root directory first and that you have python 3.10 installed.

Create a `venv` environment:

```bash
python3 -m venv .venv
```

Activate `venv` environment:

```bash
source .venv/bin/activate
```

Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Deactivate `venv` environment:

```bash
deactivate
```

#### How to run the program

Make sure you are in the repo's root directory first.

```bash
python3 madlib_cli/madlib.py
```

#### How to run all the tests in the repository

Make sure you are in the repo's root directory first.

```bash
pytest -v
```