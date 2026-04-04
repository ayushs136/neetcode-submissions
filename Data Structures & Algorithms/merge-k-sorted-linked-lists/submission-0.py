# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        n = len(lists)
        if n == 0:
            return None
        if n==1:
            return lists[0]

        mid = n //2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.merge(left, right)

    def merge(self, li1, li2):

        dummy = ListNode(-1)
        curr = dummy

        while li1 and li2:

            if li1.val < li2.val:
                curr.next = li1
                li1 = li1.next
            else:
                curr.next = li2
                li2 = li2.next

            curr = curr.next

        curr.next = li1 if li1 else li2

        return dummy.next