#  Valid Palindrome II

# DESCRIPTION
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# EXAMPLE
# Example 1:
# Input: s = "aba"
# Output: true
# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:
# Input: s = "abc"
# Output: false

# CONSTRAINTS
# 1 <= s.length <= 105
# s consists of lowercase English letters.

# SOLUTION
class Solution:
  def validPalindrome(self, s: str) -> bool:
    # Helper function to check palindrome in a given range
    def is_palindrome(left: int, right: int) -> bool:
      while left < right:
        if s[left] != s[right]:
          return False
        left += 1
        right -= 1

      return True

    left = 0
    right = len(s) - 1

    while left < right:
      # If characters match, move inward
      if s[left] == s[right]:
        left += 1
        right -= 1
      else:
        # Skip either left or right character once
        return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)

    return True

