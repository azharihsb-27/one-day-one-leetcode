#  Longest Common Prefix

# DESCRIPTION
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# EXAMPLE
# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

# CONSTRAINTS
# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

# SOLUTION
class Solution:
  def lengthOfLastWord(self, s: str) -> int:
    last = 0  # Counter to store the length of the last word

    # Loop from the end of the string to the beginning
    for i in range(len(s) - 1, -1, -1):

      # Skip trailing spaces before the last word starts
      if s[i] == ' ' and last == 0:
        continue

      # If a space is found after counting characters,
      # It means the last word has ended
      elif s[i] == ' ' and last != 0:
        break

      # Count characters of the last word
      else:
        last += 1

    return last  # Return the length of the last word
