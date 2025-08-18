# 1323. Maximum 69 Number
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a positive integer num consisting only of digits 6 and 9.

# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

 

# Example 1:

# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.
# Example 2:

# Input: num = 9996
# Output: 9999
# Explanation: Changing the last digit 6 to 9 results in the maximum number.
# Example 3:

# Input: num = 9999
# Output: 9999
# Explanation: It is better not to apply any change.
 

# Constraints:

# 1 <= num <= 104
# num consists of only 6 and 9 digits.

class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)
        n = len(str_num)
        for i in range(n):
            if str_num[i] == '6':
                return num + (3* (10**(n-i-1)))
        return num

# class Solution:
#     def maximum69Number (self, num: int) -> int:
#         num_list = list(str(num))
#         n = len(num_list)
#         for i in range(n):
#             if num_list[i] == '6':
#                 num_list[i] = '9'
#                 return int("".join(num_list))
#         return num
sol = Solution()
print(sol.maximum69Number(9669))
print(sol.maximum69Number(9996))
print(sol.maximum69Number(9999))