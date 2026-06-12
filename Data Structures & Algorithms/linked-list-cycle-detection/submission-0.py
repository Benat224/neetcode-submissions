# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        conjunto = set()
        cur = head
        while cur  and cur not in conjunto:
            conjunto.add(cur)
            cur = cur.next
        return cur != None
        