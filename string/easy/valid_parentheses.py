#  Longest Common Prefix

# DESCRIPTION
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# EXAMPLE
# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "()[]{}"
# Output: true
# Example 3:
# Input: s = "(]"
# Output: false
# Example 4:
# Input: s = "([])"
# Output: true
# Example 5:
# Input: s = "([)]"
# Output: false

# CONSTRAINTS
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# SOLUTION
class Solution:
  def isValid(self, s: str) -> bool:
    # Stack to store opening brackets
    stack = []

    # Mapping of closing brackets to their matching opening brackets
    pairs = {
      ')': '(',
      ']': '[',
      '}': '{'
    }

    # Iterate through each character in the string
    for ch in s:
      # If the character is an opening bracket
      if ch in pairs.values():
        stack.append(ch)
      else:
        # If there is no opening bracket to match
        if not stack:
          return False

        # Pop the last opening bracket
        top = stack.pop()

        # Check if it matches the current closing bracket
        if top != pairs[ch]:
          return False

    # At the end, stack should be empty if all brackets are valid
    return not stack

