# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        cur = head
        end = False
        for i in range(k):
            if cur:
                cur = cur.next
            else:
                end = True
                break
        if end:
            return head
        else:
            cur = head.next
            last = head
            for i in range(k - 1):
                temp = None
                if cur.next:
                    temp = cur.next
                cur.next = last
                last = cur
                cur = temp
            head.next = self.reverseKGroup(cur, k)
            return last
