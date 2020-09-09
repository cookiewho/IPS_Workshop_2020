'''
Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the
first two lists.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = None
        while l1!= None or l2 != None:
            if l1 == None:
                if (curr == None):
                    head = ListNode(l2.val, None)
                    curr = head
                else:
                    curr.next = ListNode(l2.val, None)
                    curr = curr.next
                l2 = l2.next
            elif l2 == None:
                if (curr == None):
                    head = ListNode(l1.val, None)
                    curr = head
                else:
                    curr.next = ListNode(l1.val, None)
                    curr = curr.next
                l1 = l1.next
            elif l1.val <= l2.val:
                if (curr == None):
                    head = ListNode(l1.val, None)
                    curr = head
                else:
                    curr.next = ListNode(l1.val, None)
                    curr = curr.next
                l1 = l1.next
            else:
                if (curr == None):
                    head = ListNode(l2.val, None)
                    curr = head
                else:
                    curr.next = ListNode(l2.val, None)
                    curr = curr.next
                l2 = l2.next
        if curr == None:
            return curr
        return head