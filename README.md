# Usage
## Local install (python >=3.6)

(optional) Create and activate venv:
  - `python -m venv env`
  - `source env/bin/activate`

Pip install `phrases`
  - `pip install -e .`
  - `cat file1.txt | phrases` or `phrases file1.txt`

A test has been provided `src/phrases/test_top_ten.py`
  - `python src/phrases/test_top_ten.py`

## Dockerfile
A dockerfile has been provided that operates in three stages. My favorite part about docker multi-stage builds is no artifact is produced if any stage fails (build-time testing!!).

Build docker container
  - `docker build --rm -f Dockerfile -t phrases:latest .`