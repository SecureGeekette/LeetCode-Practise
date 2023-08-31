11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

Solution:

Brute Force - O(n^2)

class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_water = 0
        cur_water = 0

        for i in range(len(height)):
            for j in range(i+1,len(height)):

                cur_water = min(height[i], height[j])*(j-i)
                if max_water < cur_water:
                    max_water = cur_water

        return max_water

  This solution although correct, won't work on all test cases - Time Limit Exceeded Error


O(n) solution - Logic remains the same but we only need to compare the heights each time, this can be done in 1 loop

class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_water = 0
        cur_water = 0
        
        l = 0
        r = len(height)-1

        while l < r:

            cur_water = min(height[l], height[r])*(r-l)
            if max_water < cur_water:
                max_water = cur_water

            if height[l] <= height[r]:
                l = l+1
            else:
                r = r-1 

        return max_water
