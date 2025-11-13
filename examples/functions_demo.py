def greet(name: str = "World") -> str:
    """返回问候语"""
    return f"Hello, {name}!"

def divide(a: float, b: float) -> float:
    """安全的除法，捕获异常"""
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("除数不能为 0")

if __name__ == "__main__":
    print(greet())
    print(greet("Python"))
    print("10 / 2 =", divide(10, 2))
    try:
        divide(5, 0)
    except ValueError as e:
        print("捕获异常:", e)