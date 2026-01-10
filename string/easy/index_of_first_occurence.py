#  Contains Duplicate

# DESCRIPTION
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# EXAMPLE
# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

# CONSTRAINTS
# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.

# SOLUTION
class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    # Check if the substring 'needle' exists in 'haystack'
    if needle in haystack:
      # Return the index of the first occurrence of 'needle'
      return haystack.index(needle)

    # Return -1 if 'needle' is not found
    return -1


