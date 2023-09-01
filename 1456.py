1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Solution:

#Brute force, O(n^2) - time exceeded
class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        max_vowels = 0

        vowels = "aeiou"

        for i in range(0, len(s)-k+1):
            cur_vowels = 0
            for char in s[i:i+k]:
                if char in vowels:
                    cur_vowels += 1
            if max_vowels < cur_vowels:
                max_vowels = cur_vowels
                if max_vowels == k:
                    return max_vowels

        return max_vowels
        

