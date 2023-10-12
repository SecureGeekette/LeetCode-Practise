88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109

It's very easy to solve this using O(n) extra memory i.e. keep comparing both arrays and add them in a sorted fashion to a third array and then add these back to nums1 for output, but since we can't do that we need to do in-place sorting

1st attempt (47/59 testcases passed):
Baiscally comparing both arrays and if number is from nums2 then we move everything from idx onwards by 1 i.e. push to right, but there seem to be a lot of edge cases here

What I missed in this solution is time complexity, in the worst case if everything in nums2 is lesser than everything in nums1, so each time we need to push all elements to the right which is O(n) for each element in nums 2, so O(n^2).

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = 0
        j = 0

        if n != 0:   
            while i < m+n and j < n:
                if m == 0:
                    nums1[i] = nums2[j]
                    i += 1
                    j += 1
                elif nums1[i] == 0 and i >= m:
                    nums1[i] = nums2[j]
                    i+=1
                    j+=1
                elif nums1[i] <= nums2[j]:
                    i += 1
                elif nums1[i] > nums2[j]:
                    for idx in range(m+n-2,i-1,-1):
                        nums1[idx+1] = nums1[idx]
                    nums1[i] = nums2[j]
                    j+=1


Saw solution (Neetcode) - we should be comparing from end of array since both the arrays are already in sorted order

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        last = m+n-1
        i = m-1
        j = n-1

        while i >= 0 and j >= 0:

            if nums1[i] < nums2[j]:
                nums1[last] = nums2[j]
                j -= 1
            else:
                nums1[last] = nums1[i]
                i -=1

            last -=1

        while j >= 0:
            nums1[last] = nums2[j]
            j -= 1
            last -= 1


