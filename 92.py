92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prev_left, curr = dummy, head

        # to reach the left node of the linked list
        for i in range(left-1):
            prev_left = curr
            curr = curr.next

        prev = None
        # reverse the nodes between left and right of the linked list
        for i in range(right-left+1):
            temp_next = curr.next
            curr.next = prev
            prev, curr = curr, temp_next

        prev_left.next.next = curr
        prev_left.next = prev

        return dummy.next

