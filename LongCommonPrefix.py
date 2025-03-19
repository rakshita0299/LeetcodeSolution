class Solution:
  def longestCommonPrefix(self, strs):
    self.strs=strs
    if not strs:
      return ''

    for i in range(len(strs[0])):
      for k in range(1, len(strs)):
        if i == len(strs[k]) or strs[k][i] != strs[0][i]:
          return strs[0][:i]

    return strs[0]