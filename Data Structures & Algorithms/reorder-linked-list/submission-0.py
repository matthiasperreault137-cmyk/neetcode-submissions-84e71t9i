# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        n = 0
        linklist = []
        while cur:
            linklist.append(cur)
            cur = cur.next
            n += 1
        if n % 2 == 1:
            firsthalf = linklist[:(n//2) + 1]
            lasthalf = linklist[(n//2) + 1:]
            i = 0
            while len(lasthalf) - 1 - i >= 0:
                firsthalf[i].next = lasthalf[len(lasthalf) - 1 - i]
                lasthalf[len(lasthalf) - 1 - i].next = firsthalf[i + 1]
                i += 1
            if i < len(firsthalf):
                firsthalf[i].next = None
        else:
            firsthalf = linklist[:(n//2)]
            lasthalf = linklist[n//2:]
            i = 0
            while i < len(firsthalf):
                firsthalf[i].next = lasthalf[len(lasthalf) - 1 - i]
                if i + 1 < len(firsthalf): 
                    lasthalf[len(lasthalf) - 1 - i].next = firsthalf[i + 1]
                else:
                    lasthalf[len(lasthalf) - 1 - i]. next = None
                i += 1
        return None