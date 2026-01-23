#  Find All Numbers Disappeared in an Array

# DESCRIPTION
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# EXAMPLE
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:
# Input: nums = [1,1]
# Output: [2]

# CONSTRAINTS
# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n

# SOLUTION
# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

class Solution:
  def findDisappearedNumbers(self, nums):
    # First loop: mark numbers that appear in the array
    for i in range(len(nums)):
      # Use absolute value since elements may already be marked (negative)
      idx = abs(nums[i]) - 1
      
      # Mark the index as negative to indicate the number exists
      if nums[idx] > 0:
        nums[idx] = -nums[idx]

    # Second loop: collect numbers that never appeared
    result = []
    for i in range(len(nums)):
      # A positive value means the number (i + 1) was never marked
      if nums[i] > 0:
        result.append(i + 1)

    return result

