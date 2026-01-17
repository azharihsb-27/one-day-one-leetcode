#  Reverse Vowels of a String

# DESCRIPTION
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# EXAMPLE
# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"
# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

# CONSTRAINTS
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

# SOLUTION
class Solution:
  def reverseVowels(self, s: str) -> str:
    # Set vowels
    vowels = set("aeiouAEIOU")
    # Convert string to list because string is immutable in Python
    chars = list(s)
    left, right = 0, len(chars) - 1

    while left < right:
      # Move left pointer until it points to a vowel
      if chars[left] not in vowels:
        left += 1
      # Move right pointer until it points to a vowel
      elif chars[right] not in vowels:
        right -= 1
      else:
        # If both pointers are at vowels,then swap
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    # Convert list back to string
    return "".join(chars)

