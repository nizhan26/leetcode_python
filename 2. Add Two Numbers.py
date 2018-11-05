
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Complexity
#T: O(n1+n2)
#S: O(n1+n2)
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None
    
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        
        Example:
        Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 0 -> 8
        Explanation: 342 + 465 = 807.
        """
        
  
        result = ListNode(0)
        current, carry = result, 0
        
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
                
            carry, val = divmod(val,10)
            current.next = ListNode(val)
            current = current.next
            
        if carry:
            current.next = ListNode(1)
        
        return result.next
                
