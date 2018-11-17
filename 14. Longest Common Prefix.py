'''

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example:
Input: ["flower","flow","flight"]
Output: "fl"
'''

class Solution:
  def longestCommonPrefix(self, s):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(s) == 0: return ''
        if len(s) == 1: return s[0]
        
        #sort strings by alphabetical order
        #窝草太机智了
        s = sorted(s)
        
        s1, s2 = s[0], s[-1]
        prefix = ''
        
        for i in range(min(len(s1), len(s2)):
            if s1[i] == s2[i]:
                prefix += s1[i]
            else: break
        
        return prefix
