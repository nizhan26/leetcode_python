#Description:
#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#Example 1:
#Input: "babad"
#Output: "bab"
#Note: "aba" is also a valid answer.


#T: O(n)
#S: O(c)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s = len(s)
        max_len, st = 1, 0
        
        if len_s < 2 or s == s[::-1]:
            return s
        
        for i in range(len_s):
            test_1 = s[i-max_len-1:i+1]
            test_2 = s[i-max_len:i+1]
            
            if i-max_len-1>=0 and test_1 == test_1[::-1]:
                max_len += 2
                start = i-max_len-1
                continue
            if i-max_len>=0 and test_2 = test_2[::-1]:
                max_len += 1
                start = i-max_len
                
        return s[start:start+max_len]
