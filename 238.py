238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Solution I tried (this uses division and satisfies 19/22 test cases) - we have to work with each edge case for this - not recommended

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = 1
        output = []
        found_0 = 0
        zeroes = 1
        
        for i in range(len(nums)):
            output.append(0)
            if nums[i] != 0:
                product = product*nums[i]
                zeroes = 0
            if nums[i] == 0:
                found_0 = 1

        if zeroes == 1:
            return output

        for i in range(len(nums)):
            if found_0 == 1 and nums[i] == 0:
                output[i] = product
                break
            elif found_0 == 1:
                output[i] = 0
            elif nums[i] != 0:
                output[i] = int(product/nums[i])  

        return output    

