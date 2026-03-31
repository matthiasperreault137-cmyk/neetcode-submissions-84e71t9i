# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n > 0 and (head is None or head.next is None):
            return None
        first = head
        last = head
        for i in range(n - 1):
            first = first.next
        if first.next is None:
            return last.next
        first = first.next
        while first.next:
            last = last.next
            first = first.next
        temp = last
        last = last.next.next
        temp.next = last
        return head
        