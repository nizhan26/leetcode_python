#Description:
#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#Example 1:
#Input: "babad"
#Output: "bab"
#Note: "aba" is also a valid answer.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #insert '#'s to standarize the odd and even cases
        sl = '#'
        #for example #a#b# (2->5); #a#b#c#(3->6)
        for c in s:
            sl = sl + c + '#'
        #roc[i] is the longest length of palidrome centered by i
        roc = [0] * len(sl)
        
        rl = 0
        res = ''
        i = 0
        mi = 0
        mx = 0
        
        for i in range(len(sl)):
            roc[i] = min(mx - i, roc[2*mi-i]) if i < mx else 0
            l = i-roc[i]
            r = i+roc[i]
            while(l-1 >= 0 and r+1 < len(sl) and sl[l-1] == sl[r+1]):
                roc[i] += 1
                l -= 1
                r += 1
            if roc[i] >= rl:
                res = s[l//2 : (l//2 + roc[i])]
                rl = roc[i]
            if i + roc[i] > mx:
                mx = i + roc[i]
                mi = i
            i += 1
            
        return res
        
        
        
        longest, start, low, high, n = 1, 0, 0, 0, len(s)
        n = len(s)
        for i in range(1, n):
            
            low = i-1
            high = i+1
            while low >= 0 and high < n and s[low] == s[high]:
                if (high - low + 1) >= longest:
                    longest = high - low + 1
                    start = low
                low -= 1
                high += 1
                
            #even palidrome
            low = i-1
            high = i
            while low >= 0 and high < n and s[low] == s[high]:
                if (high - low + 1) >= longest:
                    longest = high - low + 1
                    start = low
                low -= 1
                high += 1
                
        return s[start: start + longest]
    
