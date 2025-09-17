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



# -------------------- Math Library --------------------

class MultiplyRequest(BaseModel):
    x: float = Field(..., description="First factor")
    y: float = Field(..., description="Second factor")


class PowerRequest(BaseModel):
    base: float = Field(..., description="Base value")
    exponent: float = Field(..., description="Exponent value")


class FactorialRequest(BaseModel):
    n: int = Field(..., ge=0, description="Non-negative integer for factorial")


def compute_add(x: float, y: float) -> float:
    return x + y


def compute_multiply(x: float, y: float) -> float:
    return x * y


def compute_power(base: float, exponent: float) -> float:
    return base ** exponent


def compute_factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


@app.get("/math/add")
def add(x: float, y: float):
    return {"result": compute_add(x, y)}


@app.post("/math/multiply")
def multiply(req: MultiplyRequest):
    return {"result": compute_multiply(req.x, req.y)}


@app.put("/math/power")
def power(req: PowerRequest):
    return {"result": compute_power(req.base, req.exponent)}


@app.patch("/math/factorial")
def factorial(req: FactorialRequest):
    return {"result": compute_factorial(req.n)}

