# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            mid = len(lists) // 2
            list1 = self.mergeKLists(lists[:mid])
            list2 = self.mergeKLists(lists[mid:])
            merged = self.merge(list1, list2)
            return merged


    def merge(self, list1, list2):
        dummy = node = ListNode(0)
        while list1 and list2:
            if list1.val > list2.val:
                node.next = list2
                list2 = list2.next
            else:
                node.next = list1
                list1 = list1.next
            node = node.next
        node.next = list1 or list2
        return dummy.next
                


