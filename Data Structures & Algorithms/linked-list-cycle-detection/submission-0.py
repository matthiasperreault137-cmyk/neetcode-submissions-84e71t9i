# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        left = head
        right = head.next
        while right and right.next:
            if right == left:
                return True
            else:
                right = right.next.next
                left = left.next
        return False