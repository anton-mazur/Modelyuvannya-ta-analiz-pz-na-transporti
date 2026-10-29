from collections import Counter


def first_uniq_char(s: str) -> int:
    counts = Counter(s)
    for index, character in enumerate(s):
        if counts[character] == 1:
            return index
    return -1


if __name__ == "__main__":
    print(first_uniq_char("leopard"))
    print(first_uniq_char("loveleopard"))
    print(first_uniq_char("aabb"))
