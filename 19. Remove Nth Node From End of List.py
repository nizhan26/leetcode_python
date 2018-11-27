#Given a linked list, remove the n-th node from the end of list and return its head.

#Example:

#Given linked list: 1->2->3->4->5, and n = 2.

#After removing the second node from the end, the linked list becomes 1->2->3->5.

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        #Solution 1: staright forward. scan the list to get the length, scan again to locate the required position.
        length, dummy = 0, ListNode(-1)
        dummy.next = head
        p = dummy
        
        while p.next:
            length += 1
            p = p.next
            
        if n >= length:
            return head.next
        
        p = dummy
        for i in range(length - n):
            p = p.next
        p.next = p.next.next
        
        return head
        
        #Solution 2: faster, set up 2 pointers
        
        fast = slow = head
        
        for i in range(n):
            fast = fast.next
        #if the position does not exist, eliminate the first element    
        if not fast:
            return head.next
            
        #move two pointers together
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        #Now slow is at the right position
        slow.next = slow.next.next
        
        return head
