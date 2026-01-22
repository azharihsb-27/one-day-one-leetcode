#  Missing Number

# DESCRIPTION
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# EXAMPLE
# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation:
# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation:
# n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation:
# n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

# CONSTRAINTS
# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# All the numbers of nums are unique.

# SOLUTION
# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    # n is the length of the array
    n = len(nums)

    # Expected sum of numbers from 0 to n
    # Formula: n * (n + 1) // 2
    expected = n * (n + 1) // 2

    # Actual sum of elements in the array
    actual = sum(nums)

    # The missing number is the difference
    return expected - actual
