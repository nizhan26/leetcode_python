'''
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
'''

 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
         
 class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = p = ListNode(0)
        dummy.next = head
        first = head
        second = first.next
        
        while first and second:
            first.next = second.next
            second.next = first
            p.next = second
            
            p = first
            first = first.next
            if not first:
                break
            second = first.next
        return dummy.next
