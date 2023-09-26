28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


First attempt:

        list_needle = list(needle)
        list_haystack = list(haystack)

        len_n = len(list_needle)
        len_h = len(list_haystack)

        n = 0
        h = 0

        while n < len_n and h < len_h and list_needle[n] != list_haystack[h]:
            h += 1
            n = 0        
        while n < len_n and h < len_h and list_needle[n] == list_haystack[h]:
            n += 1
            h += 1
        if n == len_n:
            return h - n
        elif h == len_h:
            return -1

Mistake: Did not try enough test cases - this passed only 64/82 test cases. We have to do the whiles in an if/ else condition but I didn't know how to solve this. Looked at the solution in ChatGPT.

Final solution:

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        len_n = len(needle)
        len_h = len(haystack)

        for h in range(len_h-len_n+1):
            if haystack[h: h+len_n] == needle:
                return h
        
        return -1

