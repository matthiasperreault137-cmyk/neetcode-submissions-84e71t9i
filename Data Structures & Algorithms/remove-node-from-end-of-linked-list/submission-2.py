# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n > 0 and (head is None or head.next is None):
            return None
        size = 0
        cur = head
        while cur:
            cur = cur.next
            size += 1
        steps = size - n
        cur = head
        if steps == 0:
            return head.next
        for i in range(steps - 1):
            cur = cur.next
        temp = cur
        cur = cur.next.next
        temp.next = cur
        return head