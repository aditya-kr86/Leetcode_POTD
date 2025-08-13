# 326. Power of Three
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

 

# Example 1:

# Input: n = 27
# Output: true
# Explanation: 27 = 33
# Example 2:

# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.
# Example 3:

# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).
 

# Constraints:

# -231 <= n <= 231 - 1
 
# Brute Force
# Follow up: Could you solve it without loops/recursion?
# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         def decimalToBase3(n):
#             if n == 0:
#                 return "0"
#             trinary_string = ""
#             while n>0:
#                 remainder = n%3
#                 trinary_string = str(remainder) + trinary_string
#                 n = n // 3
#             # print(trinary_string)
#             return trinary_string
#         if n < 1:
#             return False
#         count = 0
#         base3 = decimalToBase3(n)
#         for ch in base3:
#             if not (ch == "1" or ch == "0"):
#                 return False
#             if ch == "1":
#                 count += 1
#                 if count > 1:
#                     return False
#         return True

# Optimized
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        else:
            while(n % 3 == 0):
                n = n//3
        return n==1
    
sol = Solution()
print(sol.isPowerOfThree(n = 27))
print(sol.isPowerOfThree(n = 0))
print(sol.isPowerOfThree(n = -1))
print(sol.isPowerOfThree(n = 19683))
print(sol.isPowerOfThree(n = 43046721))