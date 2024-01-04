118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]


Solution:
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        output = [[1]]

        for i in range(1,numRows):
            row = [0] + output[-1] + [0]
            new_row = [1]*(i+1)
            for j in range(i+1):
                new_row[j] = row[j] + row[j+1]
            output.append(new_row)

        return output
        
