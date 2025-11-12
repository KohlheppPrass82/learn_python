def add(a: float, b: float) -> float:
    return a + b


def mul(a: float, b: float) -> float:
    return a * b


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print(add(2, 3))
    print(mul(4, 5))
    print(factorial(5))
