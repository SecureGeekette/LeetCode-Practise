242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false


Solution:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dict_s = {}

        for char in s:
            if char in dict_s:
                dict_s[char] += 1
            else:
                dict_s[char] = 1

        for char in t:
            if char in dict_s:
                dict_s[char] -= 1
            else:
                return False

        for values in dict_s.values():
            if values != 0:
                return False

        return True
        
