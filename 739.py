739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Input: temperatures = [30,60,90]
Output: [1,1,0]


Solution:
Brute Force - O(n2)

 answer = []

     for i in range(len(temperatures)):
          found = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    answer.append(j-i)
                    found = 1
                    break
            if found == 0:
                answer.append(0)

        return answer

Monotonic Stack - O(n)

        answer = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackt, stackindex = stack.pop()
                answer[stackindex] = i-stackindex    
            stack.append([t,i])


        return answer


Learning/ Mistakes:
Learnt the concept of monotonic stack for the first time.
