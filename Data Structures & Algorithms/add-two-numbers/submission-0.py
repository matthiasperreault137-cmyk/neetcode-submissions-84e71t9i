# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mult = 1
        cur1 = l1
        cur2 = l2
        total = 0
        while cur1 or cur2:
            if cur1:
                total += cur1.val * mult
                cur1 = cur1.next
            if cur2:
                total += cur2.val * mult
                cur2 = cur2.next
            mult *= 10
        cur = ListNode(total % 10)
        head = cur
        total //= 10
        while total > 0:
            new = ListNode(total % 10)
            cur.next = new
            cur = cur.next
            total //= 10
        return head
