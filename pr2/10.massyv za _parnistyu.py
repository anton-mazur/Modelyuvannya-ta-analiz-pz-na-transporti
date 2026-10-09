def funkcia(nums: list[int]) -> list[int]:
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] % 2 == 0:
            left += 1
        elif nums[right] % 2 == 1:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums


if __name__ == "__main__":
    tests = [
        ([3, 1, 2, 4], [3, 1, 2, 4]),
        ([0], [0]),
        ([1], [1]),
        ([2, 4, 6], [2, 4, 6]),
        ([1, 3, 5], [1, 3, 5]),
        ([0, 1, 2, 3, 4], [0, 1, 2, 3, 4]),
    ]

    for number, (nums, original) in enumerate(tests, start=1):
        result = funkcia(nums)
        first_odd = next(
            (index for index, value in enumerate(result) if value % 2 == 1),
            len(result),
        )
        assert all(value % 2 == 0 for value in result[:first_odd]), (
            f"Тест {number}: парне число опинилося після непарного: {result}"
        )
        assert all(value % 2 == 1 for value in result[first_odd:]), (
            f"Тест {number}: непарне число опинилося перед парним: {result}"
        )
        assert sorted(result) == sorted(original), (
            f"Тест {number}: змінився набір елементів: {result}"
        )
        print(f"Тест {number} пройдено: {result}")