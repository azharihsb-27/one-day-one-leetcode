#  Contains Duplicate

# DESCRIPTION
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

# EXAMPLE
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

# CONSTRAINTS
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

# SOLUTION
class Solution:
  def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # Convert both lists to sets to remove duplicates
    set1 = set(nums1)
    set2 = set(nums2)

    # List to store the intersection result
    res = []

    # Iterate through unique elements in set1
    for num in set1:
      # Check if the number also exists in set2
      if num in set2:
        # If yes, add it to the result
        res.append(num)

    # Return the list of common elements
    return res

