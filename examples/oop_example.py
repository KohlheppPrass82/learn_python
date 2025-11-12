class Counter:
    def __init__(self, start: int = 0):
        self.value = start

    def increment(self, step: int = 1) -> int:
        self.value += step
        return self.value

    def reset(self) -> None:
        self.value = 0

    def __repr__(self) -> str:
        return f"Counter(value={self.value})"


if __name__ == "__main__":
    c = Counter()
    print(c)
    c.increment()
    c.increment(5)
    print(c)
    c.reset()
    print(c)
