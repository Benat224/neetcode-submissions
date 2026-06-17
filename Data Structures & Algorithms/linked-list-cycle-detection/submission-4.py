# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1  = head
        if not head:
            return False
        p2 = p1.next
        while p1 and p2 and p1.val != p2.val:
            p1 = p1.next
            if not p2.next:
                return False
            p2= p2.next.next
        if p1 and p2:
            return True
        return False