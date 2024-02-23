1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Solution

1. Brute Force (O(n^2)) time and O(1) space

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        first_idx, second_idx = 0, 1

        for first_idx in range(len(nums)):
            for second_idx in range(first_idx+1, len(nums)):
                if nums[first_idx] + nums[second_idx] == target:
                    return [first_idx, second_idx]


2. Hash Map (O(n)) solution time and 0(n) space

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_val = {}

        for i in range(len(nums)):
            search_val = target - nums[i]
            if search_val in hash_val:
                return [hash_val[search_val], i]
            else:
                hash_val[nums[i]] = i

