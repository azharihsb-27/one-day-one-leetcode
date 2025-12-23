#  Longest Common Prefix

# DESCRIPTION
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# EXAMPLE
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# CONSTRAINTS
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

# SOLUTION
class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    com_pref = ""
    sorted_strs = sorted(strs)
    first_pref = sorted_strs[0]
    last_pref = sorted_strs[-1]

    for i in range(min(len(first_pref), len(last_pref))):
      if first_pref[i] != last_pref[i]:
        return com_pref
      else:          com_pref += first_pref[i]

    return com_pref