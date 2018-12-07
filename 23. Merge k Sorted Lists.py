'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #Solution 1: Recursion
        #Time: O(nlogk)
        #Space: O(logk)
        
        return self.helper(lists, 0, len(lists) - 1)
        
    def helper(self, lists, begin, end):
        if begin > end:
            return None
        if begin == end:
            return lists[begin]
        return self.mergeTwo(self.helper(lists, begin, (begin + end) // 2), self.helper(lists, (begin+end) //2 + 1, end))
        
    def mergeTwoLists(self, l1, l2):
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2    #good!
        return dummy.next
        
        
        
        #Solution 2
        #cheating genius
        
        temp = []
        for x in lists:
            linked_list = []
            while x:
                linked_list.append(x.val)
                x = x.next
            temp.extend(linked_list)
        
        dummy = res = ListNode(0)
        for i in sorted(temp):
            dummy.next = ListNode(i)
            dummy = dummy.next
        
        return res.next
        
        #Solution 3
        #unreadable, but simple logic
        if not any(lists):  #all empty
            return None
        elif len(lists) == 1:
            return lists[0]
        lists = [node for node in lists if node]
        tempList = [node.val for node in lists]
        result = ListNode(-float('inf'))
        Item = result
        while tempList != []:  #valid numbers are in tempList
            currentMin = min(tempList)
            Item.next = ListNode(currentMin)
            Item = Item.next
            lists[tempList.index(currentMin)] = lists[tempList.index(currentMin)].next
            
            if lists[tempList.index(currentMin)] == None:
                lists.remove(lists[tempList.index(currentMin)])
            tempList = [node.val for node in lists if node]
        return result.next
        
