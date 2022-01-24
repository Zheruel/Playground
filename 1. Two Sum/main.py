from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hash_map = {nums[i]: i for i in range(len(nums))}
    indices = []

    for i, num in enumerate(nums):
        search_target = target - num
        hash_check = hash_map.get(search_target)

        if hash_check != None and hash_check != i:
            indices.append(i)
            indices.append(hash_check)

            return indices


nums = [3, 3]
target = 6

print(twoSum(nums, target))
