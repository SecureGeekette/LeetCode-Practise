21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]


Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        current = dummy

        cur_list1 = list1
        cur_list2 = list2

        while cur_list1 is not None and cur_list2 is not None:
            if cur_list1.val > cur_list2.val:
                current.next = cur_list2
                cur_list2 = cur_list2.next
            else:
                current.next = cur_list1
                cur_list1 = cur_list1.next

            current = current.next

        if cur_list1 is not None:
            current.next = cur_list1
        
        if cur_list2 is not None:
            current.next = cur_list2

        return dummy.next


Mistakes:
Did a while and traversed the rest of the linked list when 1 linked list is over which is unnecessary, we can just point to the remaining linked list.
Also don't have a grasp on linked list yet, need to solve a couple more of easy's.
