# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        curr = head
        previous = None
        while curr:

            next = curr.next
            curr.next = previous
            previous = curr
            curr = next
        
        return previous

    def getKthNode(self, node, k):

        while node and k>1:
            k-=1
            node = node.next

        return node

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        temp = head
        previous = None

        while temp:

            kthNode = self.getKthNode(temp, k)

            if not kthNode:
                if previous:
                    previous.next = temp
                break   

            next = kthNode.next
            kthNode.next = None

            reversedHead = self.reverse(temp)

            if temp == head:
                head = kthNode
            else:
                previous.next = reversedHead

            previous = temp
            temp = next

        return head
            



    