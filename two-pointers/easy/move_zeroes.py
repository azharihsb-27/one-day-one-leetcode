#  Merge Sorted Array

# DESCRIPTION
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# EXAMPLE
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]

# CONSTRAINTS
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

# SOLUTION
class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    j = 0  # Index where the next non-zero element should be placed

    for i in range(len(nums)):  # Scan array from left to right
      if nums[i] != 0:          # If current element is non-zero
        # Swap current non-zero element with the element at index j
        nums[i], nums[j] = nums[j], nums[i]
        j += 1              # Move j to the next position

