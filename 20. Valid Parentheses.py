'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
'''

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        
        #solution 1: dictionary
        stack, lookup = [], {"(" : ")", "[" : "]", "{" : "}"}
        
        for i in s:
            if i in lookup:
                stack.append(i)
            elif not stack or lookup[stack.pop()] != i:
                return False
        return not stack
  
         
        
