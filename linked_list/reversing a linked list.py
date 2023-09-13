

# reversing a linked list
class Solution:
    def reverseList(self, head:  ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt
        return prev

# using recursion
class Solution:
    def reverseList(self, head:  ListNode) -> ListNode:
    
    # recursive: T O(n), M(n)


        if not head:
            return None
    
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)

            head.next.next = head

        head.next = None

        return newHead
    

# merge two sorted lists
# defination for singly-linked list
# class ListNodes

class Solution:
    def mergeTwoLists(self, l1:ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next

            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

            if l1:
                tail.next = l1

            elif l2: #none null
                tail.next = l2

            return dummy.next





