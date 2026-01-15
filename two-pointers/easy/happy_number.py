#  Happy Number

# DESCRIPTION
# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:
# - Starting with any positive integer, replace the number by the sum of the squares of its digits.
# - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# - Those numbers for which this process ends in 1 are happy.

# Return true if n is a happy number, and false if not.

# EXAMPLE
# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:
# Input: n = 2
# Output: false

# CONSTRAINTS
# 1 <= n <= 231 - 1

# SOLUTION
class Solution:
  def isHappy(self, n: int) -> bool:
    # Set to keep track of numbers that have seen before
    seen_n = set()

    # Repeat the process until we either reach 1 or detect a loop
    while n != 1:
      # If n has appeared before, we are in a cycle
      if n in seen_n:
        return False

      # Mark current number as seen
      seen_n.add(n)

      # Compute the sum of squares of digits
      total = 0
      while n > 0:
        digit = n % 10          # Take the last digit
        total += digit * digit  # Square it and add
        n //= 10                # Remove the last digit

      # Update n with the new computed value
      n = total

    # If we exit the loop because n == 1
    return True