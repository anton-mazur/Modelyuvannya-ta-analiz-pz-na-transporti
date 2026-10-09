def funkcia(arr: list[int]) -> bool:
    if len(arr) < 3:
        return False

    peak = 0
    while peak + 1 < len(arr) and arr[peak] < arr[peak + 1]:
        peak += 1

    if peak == 0 or peak == len(arr) - 1:
        return False

    while peak + 1 < len(arr) and arr[peak] > arr[peak + 1]:
        peak += 1

    return peak == len(arr) - 1


if __name__ == "__main__":
    tests = [
        ([2, 1], False),
        ([3, 5, 5], False),
        ([0, 3, 2, 1], True),
        ([0, 1, 2, 3, 4, 2, 1], True),
        ([0, 2, 3, 3, 5, 2, 1], False),
        ([1, 2, 3], False),
        ([3, 2, 1], False),
    ]

    for number, (arr, expected) in enumerate(tests, start=1):
        result = funkcia(arr)
        assert result == expected, f"Тест {number}: {result} != {expected}"
        print(f"Тест {number} пройдено: {result}")