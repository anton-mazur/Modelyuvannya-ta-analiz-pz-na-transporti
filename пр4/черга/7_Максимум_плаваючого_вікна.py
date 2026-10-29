from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    result = []
    window = deque()

    for index, value in enumerate(nums):
        while window and window[0] <= index - k:
            window.popleft()
        while window and nums[window[-1]] <= value:
            window.pop()
        window.append(index)
        if index >= k - 1:
            result.append(nums[window[0]])

    return result
