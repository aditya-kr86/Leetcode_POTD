/*
3423. Maximum Difference Between Adjacent Elements in a Circular Array
Given a circular array nums, find the maximum absolute difference between adjacent elements.
Note: In a circular array, the first and last elements are adjacent.

Example 1:
Input: nums = [1,2,4]
Output: 3
Explanation:
Because nums is circular, nums[0] and nums[2] are adjacent. They have the maximum absolute difference of |4 - 1| = 3.

Example 2:
Input: nums = [-5,-10,-5]
Output: 5

Explanation:
The adjacent elements nums[0] and nums[1] have the maximum absolute difference of |-5 - (-10)| = 5.

Constraints:
2 <= nums.length <= 100
-100 <= nums[i] <= 100
*/

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    int maxAdjacentDistance(vector<int>& nums) {
        int n = nums.size();
        int max_dif = 0;
        for (int i = 1; i < n; i++) {
            int diff = abs(nums[i] - nums[i - 1]);
            max_dif = max(max_dif, diff);
        }
        max_dif = max(max_dif, abs(nums[n - 1] - nums[0]));
        return max_dif;
    }
};

int main() {
    Solution sol;

    vector<int> nums1 = {1, 2, 4};
    vector<int> nums2 = {-5, -10, -5};

    cout << "Output 1: " << sol.maxAdjacentDistance(nums1) << endl;
    cout << "Output 2: " << sol.maxAdjacentDistance(nums2) << endl;

    return 0;
}
