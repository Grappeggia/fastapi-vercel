from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="Fibonacci API", version="1.0.0")


class FibonacciRequest(BaseModel):
    n: int = Field(..., ge=0, description="Number of Fibonacci terms to return (non-negative integer)")


def generate_fibonacci(n: int) -> list[int]:
    """Return the first n numbers of the Fibonacci sequence as a list."""
    sequence: list[int] = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


@app.post("/fibonacci")
def fibonacci(req: FibonacciRequest):
    return {"sequence": generate_fibonacci(req.n)}


@app.get("/")
def root():
    return {"message": "Use POST /fibonacci with JSON {'n': <non-negative int>} to get the sequence."}


