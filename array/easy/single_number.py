#  Merge Sorted Array

# DESCRIPTION
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# EXAMPLE
# Example 1:
# Input: nums = [2,2,1]
# Output: 1
# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:
# Input: nums = [1]
# Output: 1

# CONSTRAINTS
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

# SOLUTION
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    num = 0         # Initialize result as 0
    for n in nums:  # Iterate through each number
      num = num ^ n # XOR current number with result

    return num      # Remaining value is the single number
