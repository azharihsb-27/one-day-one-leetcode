#  Reverse String II

# DESCRIPTION
# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

# EXAMPLE
# Example 1:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Example 2:
# Input: s = "abcd", k = 2
# Output: "bacd"

# CONSTRAINTS
# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 104

# SOLUTION
class Solution:
  def reverseStr(self, s: str, k: int) -> str:
    # Convert string to list to allow in-place modification
    s = list(s)
    n = len(s)

    # Process the string in blocks of size 2k
    for i in range(0, n, 2 * k):
      # Reverse the first k characters in the current block
      s[i:i + k] = reversed(s[i:i + k])

    # Convert list back to string
    return "".join(s)

