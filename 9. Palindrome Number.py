#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #Solution 1
        #Use the built in function
        xx = str(x)
        return xx == xx[::-1]
        
        
        #Solution 2
        #T: O(n)
        #S: O(1)
        
        xstr = str(x)
        l, r = 0, len(xstr) - 1
        while l<r:
            if xstr[l] != xstr[r]:
                return False    
            l += 1
            r -= 1
        return True
