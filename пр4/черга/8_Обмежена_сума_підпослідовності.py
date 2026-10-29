from collections import deque


def constrained_subset_sum(nums: list[int], k: int) -> int:
    dp = [0] * len(nums)
    window = deque()
    answer = float("-inf")

    for index, value in enumerate(nums):
        while window and window[0] < index - k:
            window.popleft()

        best_previous = max(0, dp[window[0]]) if window else 0
        dp[index] = value + best_previous
        answer = max(answer, dp[index])

        while window and dp[window[-1]] <= dp[index]:
            window.pop()
        window.append(index)

    return answer
