290. Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.


Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Solution:

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        hashmap = {}
        words_s = s.split()

        if len(pattern) != len(words_s):
            return False

        if len(set(list(pattern))) != len(set(words_s)):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in hashmap:
                hashmap[pattern[i]] = words_s[i]
            elif pattern[i] in hashmap:
                if hashmap[pattern[i]] != words_s[i]:
                    return False

        return True


Mistake:
Passed 39/42 test cases on first try. Still have to think of more test cases with patience.
