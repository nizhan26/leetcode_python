#Given a 32-bit signed integer, reverse digits of an integer.
#Example 1:

#Input: -123
#Output: -321



class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        #Solution 1: treat x as a number
        #T: O(n)
        #S: O(1)
        INT_MAX = 2147483647
        INT_MIN = -2147483649
        reverse = []
        
        if not x:
            return 0
        
        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)
        
        while x > 0:
            x, digit= divmod(x, 10)
            reverse.append(digit)
        
        reverse = "".join(str(i) for i in reverse)
        reverse = sign * int(reverse)
        
        if reverse > INT_MAX or reverse < INT_MIN:
            return 0
        
        return reverse
        
        
        #Solution 2: convert x to a string
        if x < 0:
            x = str(x)[1:]
            y = -int(str(x)[::-1])
        else:
            y = int(str(x)[::-1])
        if y < -2 ** 31 or y > 2 ** 31 - 1:
            return 0
        else:
            return y
          
