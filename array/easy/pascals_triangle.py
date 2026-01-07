#  Contains Duplicate

# DESCRIPTION
# Given an integer numRows, return the first numRows of Pascal's triangle.

# EXAMPLE
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
# Input: numRows = 1
# Output: [[1]]

# CONSTRAINTS
# 1 <= numRows <= 30

# SOLUTION
class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    # This list will store the entire Pascal's Triangle
    pascal = []

    # Iterate through each row number from 0 to numRows - 1
    for i in range(numRows):
      # Initialize the current row
      # The length of the row is i + 1 and
      # all values start as 1 (first and last elements are always 1)
      row = [1] * (i + 1)
      
      # Fill the inner elements of the row (excluding first and last)
      for j in range(1, i):
        # Each inner value is calculated from the previous row:
        # pascal[i - 1][j - 1] -> value from the top-left
        # pascal[i - 1][j]     -> value from the top-right
        row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

        # After the row is fully computed, add it to the triangle
        pascal.append(row)

    # Return all rows of Pascal's Triangle
    return pascal


