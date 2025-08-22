# 2348. Number of Zero-Filled Subarrays
# Given an integer array nums, return the number of subarrays filled with 0.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [1,3,0,0,2,0,0,4]
# Output: 6
# Explanation: 
# There are 4 occurrences of [0] as a subarray.
# There are 2 occurrences of [0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.

# Example 2:
# Input: nums = [0,0,0,2,0,0]
# Output: 9
# Explanation:
# There are 5 occurrences of [0] as a subarray.
# There are 3 occurrences of [0,0] as a subarray.
# There is 1 occurrence of [0,0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.

# Example 3:
# Input: nums = [2,10,2019]
# Output: 0
# Explanation: There is no subarray filled with 0. Therefore, we return 0.
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109


from typing import List
# class Solution:
#     def zeroFilledSubarray(self, nums: List[int]) -> int:
#         result = 0
#         temp = 0
#         n = len(nums)
#         prev = -1
#         for i in range(n):
#             if nums[i] == 0 and prev != 0:
#                 temp += 1
#                 prev = nums[i]
#             elif nums[i] == 0 and prev == 0:
#                 temp += 1
#                 prev = nums[i]
#             elif nums[i] != 0 and prev == 0 and temp != 0:
#                 result += (temp*(temp+1))//2
#                 prev = nums[i]
#         return result

# class Solution:
#     def zeroFilledSubarray(self, nums: List[int]) -> int:
#         temp = 0
#         result = 0
#         for num in nums:
#             if num == 0:
#                 temp += 1
#             elif temp != 0:
#                 result += (temp*(temp+1))//2
#                 temp = 0
#         if temp != 0:
#             result += (temp*(temp+1))//2
#             temp = 0
#         return result


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        j = 0
        temp = 0
        result = 0
        for num in nums:
            if num == 0:
                j += 1
                temp += j
            elif temp != 0:
                result += temp
                temp = 0
                j = 0
        if temp != 0:
            result += temp
            temp = 0
            j = 0
        return result

    
sol = Solution()
print(sol.zeroFilledSubarray(nums = [1,3,0,0,2,0,0,4]))
print(sol.zeroFilledSubarray(nums = [0,0,0,2,0,0]))
print(sol.zeroFilledSubarray(nums = [2,10,2019]))
    


