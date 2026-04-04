# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        
        dummy = ListNode(0, head)

        fast = head
        slow = dummy

        for i in range(n):
            fast = fast.next

        while fast:

            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next