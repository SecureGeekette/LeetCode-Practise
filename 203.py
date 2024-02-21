203. Remove Linked List Elements

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Input: head = [], val = 1
Output: []

Input: head = [7,7,7,7], val = 7
Output: []

Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head

        current = dummy

        while current is not None:
            if current.next is not None and current.next.val == val:
                    current.next = current.next.next
            else:
                current = current.next

        return dummy.next

  Learnings:
- Learnt we could add a dummy node for similar questions. Also was returning head which was a mistake incase it gets deleted in the code, we should've been returning dummy.next

Alternative Solution:

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        cur = head
        prev = dummy

        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        return dummy.next
