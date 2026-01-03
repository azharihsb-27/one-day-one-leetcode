#  Contains Duplicate

# DESCRIPTION
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# EXAMPLE
# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

# CONSTRAINTS
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105

# SOLUTION
class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    candidate = {}  # Store last index of each number

    for i, num in enumerate(nums):
      # If number appeared before and index distance <= k
      if num in candidate and i - candidate[num] <= k:
        return True

      # Update last index of the number
      candidate[num] = i

    return False


