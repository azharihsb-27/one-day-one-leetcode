#  Contains Duplicate

# DESCRIPTION
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# EXAMPLE
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# CONSTRAINTS
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

# SOLUTION
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    candidate = set()  # store numbers that have already appeared
    
    for num in nums:
      # if the number is already in the set, we found a duplicate. Return True
      if num in candidate:
        return True
      
      # mark this number as seen
      candidate.add(num)
    
    # no duplicate found after checking all elements, return False
    return False

