def funkcia(arr: list[int]) -> bool:
    seen: set[int] = set()
    for number in arr:
        if number * 2 in seen or (
            number % 2 == 0 and number // 2 in seen
        ):
            return True
        seen.add(number)

    return False


if __name__ == "__main__":
    tests = [
        ([10, 2, 5, 3], True),
        ([3, 1, 7, 11], False),
        ([0, 0], True),
        ([1, 1], False),
        ([-10, -5], True),
        ([-10, 5], False),
    ]

    for number, (arr, expected) in enumerate(tests, start=1):
        result = funkcia(arr)
        assert result == expected, f"Тест {number}: {result} != {expected}"
        print(f"Тест {number} пройдено: {result}")