from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        ptr1 = i + 1
        ptr2 = len(nums) - 1

        while ptr1 < ptr2:
            current_result = nums[i] + nums[ptr1] + nums[ptr2]

            if current_result < 0:
                ptr1 += 1
            elif current_result > 0:
                ptr2 -= 1
            else:
                result.append([nums[i], nums[ptr1], nums[ptr2]])
                ptr1 += 1

                while nums[ptr1] == nums[ptr1 - 1] and ptr1 < ptr2:
                    ptr1 += 1

    return result


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
