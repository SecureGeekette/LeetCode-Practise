141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

My intuitive solution was to store the visited notes in an array and if we've seen the node before, just return True. However, memory complexity and time complexity is both O(n) in this case.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        current = head
        traversed_nodes = []

        while current is not None:

            if current not in traversed_nodes:
                traversed_nodes.append(current)
                current = current.next
            else:
                return True

        return False
