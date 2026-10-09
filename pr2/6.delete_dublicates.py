def funkcia(nums: list[int]) -> int:
    if not nums:
        return 0

    unique_count = 1
    for current_index in range(1, len(nums)):
        if nums[current_index] != nums[unique_count - 1]:
            nums[unique_count] = nums[current_index]
            unique_count += 1

    return unique_count


if __name__ == "__main__":
    tests = [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([7], 1, [7]),
        ([-2, -2, -1, 0, 0], 3, [-2, -1, 0]),
    ]

    for number, (nums, expected_count, expected_unique) in enumerate(tests, start=1):
        result = funkcia(nums)
        assert result == expected_count, f"Тест {number}: {result} != {expected_count}"
        assert nums[:result] == expected_unique, (
            f"Тест {number}: {nums[:result]} != {expected_unique}"
        )
        print(f"Тест {number} пройдено: k = {result}, nums = {nums[:result]}")