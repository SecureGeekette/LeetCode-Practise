3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

Solution:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        s = list(s)
        hash_map = {}
        len_string = 0
        max_len = 0
        start = 0

        for i in range(len(s)):

            if s[i] in hash_map:
                start = max(start, hash_map[s[i]]+1)

            len_string = i - start + 1
            max_len = max(max_len, len_string)
            hash_map[s[i]] = i

        return max_len
        
