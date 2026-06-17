# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        if list1.val <= list2.val:
            head = list1
            p1 = head.next
            p2 = list2
        else:
            head = list2
            p1 = list1
            p2 = head.next
        cur = head
        while p1 and p2:
            if p1.val <= p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next
        if p1:
            cur.next = p1
        else:
            cur.next = p2
        return head

