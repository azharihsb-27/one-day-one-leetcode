#  Majority Element

# DESCRIPTION
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# EXAMPLE
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# CONSTRAINTS
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
# The input is generated such that a majority element will exist in the array.

# SOLUTION
class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    candidate = None   # Stores the current majority candidate
    count = 0          # Stores the count for the candidate

    for num in nums:
      # If count is 0, pick the current number as a new candidate
      if count == 0:
        candidate = num
        count = 1

      # If the current number matches the candidate, increase the count
      elif num == candidate:
        count += 1

      # If the current number is different, decrease the count
      else:
        count -= 1

    return candidate
