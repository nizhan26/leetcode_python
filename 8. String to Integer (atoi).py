#Description is too long, anyone intersted in this question may refer to leetcode.com, question 8

class Solution(object):
    def myAtoi(self, str):
        '''
        :type str: str
        :rtype: int
        '''
        index = 0
        res = 0
        neg = False
        int_max = pow(2, 31) - 1
        int_min = pow(-2, 31)
        str = str.strip()
        if len(str) == 0:
            return 0
            
        first = str[0]
        
        if first == '-':
            index += 1
            neg = True
        elif first == '+':
            index += 1
        elif not first.isdigit():
            return 0
        
        for i in range(index, len(str)):
            if str[i].isdigit():
                res = 10*res + (ord(str[i]) - ord('0'))
            else:
                break
                
        if res > int_max:
            if neg:
                return int_min
            else:
                return int_max
        
        if neg:
            return -res
        return res
        
