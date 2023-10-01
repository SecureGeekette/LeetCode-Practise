328. Odd Even Linked List

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:
The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106


Solution: This is my first try, I know that this is O(n) extra space and we must solve in O(1) extra space. 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        odd = []
        even = []
        current = head
        i = 1

        while current:
            if i%2 == 0:
                even.append(current)
            else:
                odd.append(current)
            current = current.next
            i += 1
        
        dummy = ListNode(0)
        if odd:
            dummy.next = odd[0]
            current = dummy.next
        else:
            return None

        for i in range(1, len(odd)):
            current.next = odd[i]
            current = current.next

        for j in range(len(even)):
            current.next = even[j]
            current = current.next

        current.next = None

        return dummy.next

Solving in O(1) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)

        if head:
            odd = head
        else:
            return None

        if head.next:
            evenHead = even = head.next
        else:
            return head

        dummy.next = odd

        while even and even.next:
            
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = evenHead

        return dummy.next
        

