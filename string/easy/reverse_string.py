#  Reverse String

# DESCRIPTION
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# EXAMPLE
# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# CONSTRAINTS
# 1 <= s.length <= 105
# s[i] is a printable ascii character.

# SOLUTION
class Solution:
  def reverseString(self, s: List[str]) -> None:
    # Initialize two pointers:
    # left starts from the beginning, right from the end
    left, right = 0, len(s) - 1

    # Swap characters while pointers have not crossed
    while left < right:
      # Swap characters at left and right indices
      s[left], s[right] = s[right], s[left]

      # Move pointers toward the center
      left += 1
      right -= 1


