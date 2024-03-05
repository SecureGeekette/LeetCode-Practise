15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Solution
  Brute Force - O(n^3)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        answer = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        possible_answer = sorted([nums[i], nums[j], nums[k]])
                        if possible_answer not in answer:
                            answer.append(possible_answer)

        return answer


Optimized solution with 2 pointer approach

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        answer = set()

        for i in range(len(nums)-2):
            start = i+1
            end = len(nums)-1
            while start < end:
                total = nums[i] + nums[start] + nums[end]
                if total < 0:
                    start += 1
                elif total > 0:
                    end -= 1
                else:
                    answer.add((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1

        return answer

