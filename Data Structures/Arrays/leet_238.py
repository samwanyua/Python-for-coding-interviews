"""
238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # solution 1: o(n)
        left_mult, right_mult = 1,1
        n = len(nums)
        left_arr, right_arr = [0] * n, [0] * n
        for i in range(n):
            j = -i - 1 # j is the index from the end of the array (i.e., right to left)
            left_arr[i] = left_mult
            right_arr[j] = right_mult
            left_mult *= nums[i]
            right_mult *= nums[j]
        return [l * r for l, r in zip(left_arr, right_arr)]

        

