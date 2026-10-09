def funkcia(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i = m - 1
    j = n - 1
    k = m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ]

    for number, (nums1, m, nums2, n, expected) in enumerate(tests, start=1):
        result = funkcia(nums1, m, nums2, n)
        assert nums1 == expected, f"Тест {number}: {nums1} != {expected}"
        assert result is None, "Функція не повинна повертати результат"
        print(f"Тест {number} пройдено: {nums1}")
