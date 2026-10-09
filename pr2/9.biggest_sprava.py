def funkcia(arr: list[int]) -> list[int]:
    greatest_to_right = -1

    for index in range(len(arr) - 1, -1, -1):
        current = arr[index]
        arr[index] = greatest_to_right
        greatest_to_right = max(greatest_to_right, current)

    return arr


if __name__ == "__main__":
    tests = [
        ([17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1]),
        ([400], [-1]),
        ([1, 2, 3], [3, 3, -1]),
        ([5, 5, 5], [5, 5, -1]),
    ]

    for number, (arr, expected) in enumerate(tests, start=1):
        result = funkcia(arr)
        assert result == expected, f"Тест {number}: {result} != {expected}"
        print(f"Тест {number} пройдено: {result}")