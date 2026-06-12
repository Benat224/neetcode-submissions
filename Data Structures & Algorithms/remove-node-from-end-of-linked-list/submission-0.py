# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        aux = head
        while aux != None:
            count += 1
            aux = aux.next
        aux = head
        num = count - n
        if num == 0:
            head = head.next
            return head 
        while num != 1:
            num -= 1
            aux = aux.next
        if aux.next != None:
            aux.next = aux.next.next
        return head

        
        