#  Excel Sheet Column Title

# DESCRIPTION
# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# EXAMPLE
# Example 1:
# Input: columnNumber = 1
# Output: "A"
# Example 2:
# Input: columnNumber = 28
# Output: "AB"
# Example 3:
# Input: columnNumber = 701
# Output: "ZY"

# CONSTRAINTS
# 1 <= columnNumber <= 231 - 1.

# SOLUTION
class Solution:
  def convertToTitle(self, columnNumber: int) -> str:
    # Store result characters (built from right to left)
    res = []

    # Process until all digits are converted
    while columnNumber > 0:
      # Convert to 0-based to correctly map 'A'–'Z'
      columnNumber -= 1
      # Get current character and append
      res.append(chr(columnNumber % 26 + ord('A')))
      # Move to the next digit
      columnNumber //= 26

    # Reverse since characters were added backwards
    return ''.join(reversed(res))



