#Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

#'.' Matches any single character.
#'*' Matches zero or more of the preceding element.
#The matching should cover the entire input string (not partial).

#Note:

#s could be empty and contains only lowercase letters a-z.
#p could be empty and contains only lowercase letters a-z, and characters like . or *.

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """ 
        
        #Solution 1: recursion
        #T: O()
        #T(n) = n*T(n-1) + c, it looks like a factorial problem(? remain to be verified)
        #S: a tree that is 2 ^ n as max
        
        if len(p) == 0: return len(s) == 0
        if len(p) == 1 or p[1] != '*':
            if len(s) == 0 or (s[0] != p[0] and p[0] != '.'):
                return False
            return self.isMatch(s[1:],p[1:])
        else:
            i, n = -1, len(s)
            while i < n and (i < 0 or p[0] == '.' or p[0] == s[i]):
                if self.isMatch(s[i+1:],p[2:]): return True
                i += 1
            return False
            
        
        #Solution 2: dp in two-dimensional list
        #T: O(m*n)
        #S: O(m*n)
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True
        
        for i in range(1, len(p) + 1):
            if p[i-1] == '*':
                if i >= 2:
                    dp[0][i] = dp[0][i-2]
        
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] = '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and s[i-1]==p[j-2] or p[j-2] == '.')
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1]==p[j-1]
                    
        return dp[len(s)][len(p)]
        
        #Solution 3:  ??
        #The complexity analysis is informal, further proof is needed
        #T: O(m*n)
        #S: O(m*n)
    
        #avoid repeating visits
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    #initialize dp(len(s), len(p)) = True, when comparation starts
                    ans = i == len(s)
                else:
                    # at least match at the first character
                    first_match = i < len(s) and p[j] in (s[i], '.')
                    if j + 1 < len(p) and p[j] == '*':
                        # '*' means repeat the character zero times or '*' matches repeating characters
                        #but first_match is confusing, cuz p[j] == '*', p[j] in (s[i], '.') can't be met simutaneously
                        ans = dp(i, j+2) or (first_match and dp(i+1, j))
                    else:
                        # else if special characters are not included, just characters match
                        ans = first_match and dp(i+1, j+1)
                memo[i,j] = ans
            return memo[i,j]
        return dp(0,0)
        
