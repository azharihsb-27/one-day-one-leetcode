#  Is Subsequence

# DESCRIPTION
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# EXAMPLE
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false

# CONSTRAINTS
# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.

# SOLUTION
class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    # Pointer untuk menandai posisi karakter yang sedang dicari di string s
    i = 0

    # Iterasi setiap karakter dalam string t
    for c in t:
      # Jika semua karakter dalam s sudah berhasil ditemukan,
      # maka s adalah subsequence dari t
      if i == len(s):
        return True

      # Jika karakter saat ini di t sama dengan karakter s[i],
      # geser pointer i untuk mencari karakter berikutnya di s
      if c == s[i]:
        i += 1

    # Setelah seluruh t ditelusuri,
    # cek apakah semua karakter s sudah ditemukan
    return i == len(s)
