'''
Given a linked list, remove the n-th node from the end of list and
return its head.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = []
        curr = head
        while curr!=None:
            l.append(curr)
            curr = curr.next
        if n == len(l):
            head = head.next
        else:
            curr = l[-(n+1)]
            curr.next = curr.next.next
        return head