# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        cur = head
        i = 0
        while cur:
            if i >= k:
                break
            else:
                cur = cur.next
                i += 1
        if i < k:
            return head
        else:
            cur = head.next
            last = head
            for i in range(k - 1):
                temp = cur.next 
                cur.next = last
                last = cur
                cur = temp
            head.next = self.reverseKGroup(cur, k)
            return last
        
                
        

            