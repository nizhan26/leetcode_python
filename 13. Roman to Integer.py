'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Example:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        sums = 0
        
        for i in range(len(s) - 1):
            if roman[s[i]] >= roman[s[i+1]]
                sums += roman[s[i]]
            else:
                sums -= roman[s[i]]
                
        return sums+roman[s[-1]]
          
