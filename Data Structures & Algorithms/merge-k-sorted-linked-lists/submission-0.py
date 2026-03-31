# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if i + 1 < len(lists):
                    list2 = lists[i + 1] 
                else:
                    list2 = None
                merged.append(self.merge(list1, list2))
            lists = merged
        return lists[0]
    def merge(self, left, right):
        dummy = ListNode()
        tail = dummy
        i = 0
        j = 0
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next   
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if right:
            tail.next = right
        if left:
            tail.next = left
        return dummy.next
                


