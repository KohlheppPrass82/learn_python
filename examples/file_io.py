from pathlib import Path


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


if __name__ == "__main__":
    p = Path(__file__).parent / "tmp.txt"
    write_text(p, "hello file")
    print(read_text(p))
