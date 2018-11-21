'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        self.dict = {'1': "", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs","8":"tuv","9":"wxyz","10":" "}
        
        if not digits:
            return []
        
        #at least one empty element in final
        final = ['']
        
        for digit in digits:
            curr = self.dict[digits]
            new = []
            for i in final:
                for j in curr:
                    new.append(i+j)
            final = new
        return final
       
