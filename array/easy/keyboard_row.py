#  Keyboard Row

# DESCRIPTION
# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

# In the American keyboard:
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

# EXAMPLE
# Example 1:
# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
# Explanation:
# Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.
# Example 2:
# Input: words = ["omk"]
# Output: []
# Example 3:
# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]

# CONSTRAINTS
# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] consists of English letters (both lowercase and uppercase). 

# SOLUTION
class Solution:
  def findWords(self, words: List[str]) -> List[str]:
    # Define keyboard rows
    row1 = "qwertyuiop"
    row2 = "asdfghjkl"
    row3 = "zxcvbnm"
    
		# Store valid words in a list
    result = []

		# Function to determine which row a character belongs to
    def get_row(char):
      # Convert to lowercase for uniformity
      char = char.lower()
      
      if char in row1:
        return 1
      elif char in row2:
        return 2
      else:
        return 3

		# Check each word
    for word in words:
      # Use the first character as the reference row
      target_row = get_row(word[0])

			# Assume the word is valid initially
      valid = True
      
			# Check each character in the word
      for ch in word:
        # If any character is in a different row, mark invalid
        if get_row(ch) != target_row:
          valid = False
          break

			# If all characters are in the same row, add to result
      if valid:
        result.append(word)

    return result
