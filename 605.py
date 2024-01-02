605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Solution:

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        cal_n = 0
        i = 0

        while i < len(flowerbed):

            if (flowerbed[i] == 0 and (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0)):
                cal_n += 1
                i+=2
            else:
                i+=1

        if cal_n >= n:
            return True
        else:
            return False


