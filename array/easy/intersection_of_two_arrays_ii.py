#  Contains Duplicate

# DESCRIPTION
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# EXAMPLE
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

# CONSTRAINTS
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

# SOLUTION
class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # List to store the intersection result
    res = []
    # Count how many times each number appears in nums2
    count = Counter(nums2)

    # Iterate through nums1
    for num in nums1:
      # Check if the number is still available in nums2
      if count[num] > 0:
        # Add the number to result
        res.append(num)
        # Decrease the count to avoid using it more than allowed
        count[num] -= 1

    # Return the final intersection list
    return res

