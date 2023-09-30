206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        nodes = []

        while current:
            nodes.append(current)
            current = current.next

        dummy = ListNode(0)

        if len(nodes) > 0:
            dummy.next = nodes[-1]
            current = dummy.next

            for i in range(len(nodes)-1, 0, -1):
                current.next = nodes[i-1]
                current = current.next
            current.next = None

        return dummy.next
        
