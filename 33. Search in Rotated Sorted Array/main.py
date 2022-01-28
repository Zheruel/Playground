from typing import List


def search(nums: List[int], target: int) -> int:
    l_ptr = 0
    r_ptr = len(nums) - 1

    while l_ptr <= r_ptr:
        mid = (l_ptr + r_ptr) // 2

        if target == nums[mid]:
            return nums[target]

        if nums[l_ptr] <= nums[mid]:
            if target > nums[mid] or target < nums[l_ptr]:
                l_ptr = mid + 1
            else:
                r_ptr = mid - 1
        else:
            if target < nums[mid] or target > nums[r_ptr]:
                r_ptr = mid - 1
            else:
                l_ptr = mid + 1

    return -1


nums = [5, 1, 3]
target = 5
print(search(nums, target))
