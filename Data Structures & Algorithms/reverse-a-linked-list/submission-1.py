# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = None
        second = head
        while second:
            aux = second.next
            second.next = first
            first = second
            second = aux
        return first
'''




class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            aux = curr.next
            curr.next = prev
            prev = curr
            curr = aux
        return prev



















class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            aux = cur.next
            cur.next = prev
            prev = cur
            cur = aux
        return prev
            







        