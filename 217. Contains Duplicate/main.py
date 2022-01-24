from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    result_dict = {}

    for num in nums:
        if num in result_dict:
            return True
        else:
            result_dict[num] = 1

    return False


nums = [1, 1, 2, 3, 4]
print(containsDuplicate(nums))
