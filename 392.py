392 - Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


Solution:

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        idx1 = 0
        idx2 = 0

        list_s = list(s)
        list_t = list(t)

        len_s = len(list_s)
        len_t = len(list_t)

        while (idx1 < len_s) and (idx2 < len_t):

            if list_s[idx1] == list_t[idx2]:
                idx1 += 1
                idx2 += 1
            else:
                idx2 += 1

        
        if idx1 == len_s:
            return True
        else:
            return False


Learning:
This is a 2 pointer question. There are 2 types of 2 pointer questions: First is same arr/ string starting comparing from beginning and end, Second is 2 different arr/strings comparing from the same direction (start/end)
