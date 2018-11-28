'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #Solution 1: resursion
        result = []
        self.helper(result, '', n, n)
        return result
        
    def helper(self, result, cur, left, right):
        #interrupt if answer is wrong
        if left > right:
            return
        if not left or not right:
            result.append(cur)
            return
        if left:
            self.helper(result, cur + "(", left - 1, right)
        if left < right:
            self.helper(result, cur + ")", left, right - 1)
