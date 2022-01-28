from typing import List


def maxProduct(nums: List[int]) -> int:
    res = max(nums)
    current_min = 1
    current_max = 1

    for n in nums:
        tmp = current_max * n
        current_max = max(tmp, n * current_min, n)
        current_min = min(tmp, n * current_min, n)

        res = max(res, current_max, current_min)

    return res


nums = [2, 3, -2, 4]
print(maxProduct(nums))
