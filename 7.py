Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
 
Constraints:
-231 <= x <= 231 - 1

Solution:
class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:
            sign = -1
        else:
            sign = 1
        
        x = abs(x)
        rev_x = 0
        while x:
            rev_x = x%10 + 10*rev_x
            x = x//10

        if rev_x > 2147483647 or rev_x < -2147483648:
            return 0
            
        return sign*rev_x
        
        
