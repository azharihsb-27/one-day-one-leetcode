#  Excel Sheet Column Number

# DESCRIPTION
# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

# EXAMPLE
# Example 1:
# Input: columnTitle = "A"
# Output: 1
# Example 2:
# Input: columnTitle = "AB"
# Output: 28
# Example 3:
# Input: columnTitle = "ZY"
# Output: 701

# CONSTRAINTS
# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"].

# SOLUTION
class Solution:
  def titleToNumber(self, columnTitle: str) -> int:
    # Initialize the result that will store the final column number
    ans = 0

    # Iterate through each character in the column title
    # map(ord, columnTitle) converts each character to its ASCII value
    for c in map(ord, columnTitle):

      # Shift the previous result to the left in base-26
      # Then add the numeric value of the current character
      # ord("A") is subtracted so that 'A' maps to 1, 'B' to 2, ..., 'Z' to 26
      ans = ans * 26 + c - ord("A") + 1

    # Return the computed column number
    return ans




