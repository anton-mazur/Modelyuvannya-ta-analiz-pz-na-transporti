def decode_string(s: str) -> str:
    counts: list[int] = []
    parts: list[str] = []
    current = []
    number = 0

    for char in s:
        if char.isdigit():
            number = number * 10 + int(char)
        elif char == "[":
            counts.append(number)
            parts.append("".join(current))
            current = []
            number = 0
        elif char == "]":
            current = [parts.pop() + "".join(current) * counts.pop()]
        else:
            current.append(char)

    return "".join(current)


if __name__ == "__main__":
    print(decode_string("3[a2[c]]"))
