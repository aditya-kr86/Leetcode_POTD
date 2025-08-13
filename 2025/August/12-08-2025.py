# 2787. Ways to Express an Integer as Sum of Powers
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given two positive integers n and x.

# Return the number of ways n can be expressed as the sum of the xth power of unique positive integers, in other words, the number of sets of unique integers [n1, n2, ..., nk] where n = n1x + n2x + ... + nkx.

# Since the result can be very large, return it modulo 109 + 7.

# For example, if n = 160 and x = 3, one way to express n is n = 23 + 33 + 53.

 

# Example 1:

# Input: n = 10, x = 2
# Output: 1
# Explanation: We can express n as the following: n = 32 + 12 = 10.
# It can be shown that it is the only way to express 10 as the sum of the 2nd power of unique integers.
# Example 2:

# Input: n = 4, x = 1
# Output: 2
# Explanation: We can express n in the following ways:
# - n = 41 = 4.
# - n = 31 + 11 = 4.
 

# Constraints:

# 1 <= n <= 300
# 1 <= x <= 5

# class Solution:
#     def numberOfWays(self, n: int, x: int) -> int:
#         num = 1
#         M = 1e9 + 7
#         def solve(n, num, x):
#             if n == 0:
#                 return 1
#             if n < 0:
#                 return 0
#             if (num**x) > n:
#                 return 0
#             else:
#                 take = solve(n-(num**x), num + 1, x)
#                 skip = solve(n, num + 1, x)
#             return (take + skip) % M
#         return solve(n, num, x)

import math

class Solution:
    def __init__(self):
        self.M = 10**9 + 7
        self.t = {}

    def solve(self, n, num, x):
        if n == 0:
            return 1
        
        if n < 0:
            return 0

        if (n, num) in self.t:
            return self.t[(n, num)]
        
        curr_power_value = int(math.pow(num, x))
        if curr_power_value > n:
            return 0

        take = self.solve(n - curr_power_value, num + 1, x)
        skip = self.solve(n, num + 1, x)
        
        self.t[(n, num)] = (take + skip) % self.M
        return self.t[(n, num)]

    def numberOfWays(self, n, x):
        self.t.clear()
        return self.solve(n, 1, x)

sol = Solution()
print(sol.numberOfWays(n = 10, x = 2))
print(sol.numberOfWays(n = 4, x = 1))