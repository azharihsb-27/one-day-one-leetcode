#  Valid Palindrome

# DESCRIPTION
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# EXAMPLE
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# CONSTRAINTS
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

# SOLUTION
class Solution:
  def isPalindrome(self, s: str) -> bool:
    # Left pointer starts at the beginning of the string
    # Right pointer starts at the end of the string
    l, r = 0, len(s) - 1

    # Continue while the two pointers have not crossed
    while l < r:

      # Move the left pointer until it points to an alphanumeric character
      while l < r and not s[l].isalnum():
        l += 1

      # Move the right pointer until it points to an alphanumeric character
      while l < r and not s[r].isalnum():
        r -= 1

      # Compare characters case-insensitively
      if s[l].lower() != s[r].lower():
        return False

      # Move both pointers toward the center
      l += 1
      r -= 1

    # If all character pairs match, the string is a palindrome
    return True
