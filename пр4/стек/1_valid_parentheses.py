def is_valid(s: str) -> bool:
    """Return True when all brackets in *s* are correctly matched."""
    pairs = {")": "(",
        "]": "[",
        "}": "{",
    }
    stack: list[str] = []

    for char in s:
        if char in "([{":
            stack.append(char)
        elif not stack or stack.pop() != pairs[char]:
            return False

    return not stack


if __name__ == "__main__":
    for value in ("()", "()[]{}", "(]"):
        print(value, is_valid(value))
