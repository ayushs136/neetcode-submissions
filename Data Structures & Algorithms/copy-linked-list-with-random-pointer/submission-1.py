class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        

        temp = head

        while temp:
            temp.next = Node(temp.val, temp.next)
            temp = temp.next.next

        temp = head

        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            else:
                temp.next.random = None
            temp = temp.next.next
        
        temp = head
        dummy = Node(-1)
        newChain = dummy
        while temp:
            newChain.next = temp.next
            temp.next = temp.next.next
            temp = temp.next
            newChain = newChain.next

        
        return dummy.next