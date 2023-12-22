509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Naive brute force solution:

class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return (self.fib(n-1) + self.fib(n-2))


No errors but runtime can be better since we are calculating fib(n-1) and fib(n-2) separately, so a lot of repition would occur

class Solution:
    def fib(self, n: int) -> int:

        fib_num = [0,1]

        if n == 0:
            return fib_num[0]
        elif n == 1:
            return fib_num[1]
        else:
            for i in range(2,n+1):
                fib_num.append(fib_num[i-1] + fib_num[i-2])

        return fib_num[n]

  Dynamic programming solution reduces runtime significantly
