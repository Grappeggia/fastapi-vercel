## Fibonacci FastAPI

Minimal FastAPI service that returns the first `n` Fibonacci numbers.

### Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Usage

- POST `http://localhost:8000/fibonacci`
- Body:

```json
{ "n": 10 }
```

- Response:

```json
{
  "sequence": [0,1,1,2,3,5,8,13,21,34]
}
```


