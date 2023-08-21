345. Reverse Vowels of a String


Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"



Solution:

class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = "aeiouAEIOU"
        s_list = list(s)
        i = 0
        j = len(s)-1
        temp = 'a'


        while i < j:
            if s[i] not in vowels and s[j] not in vowels:
                i = i+1
                j = j-1
            elif s[i] not in vowels and s[j] in vowels:
                i = i+1
            elif s[i] in vowels and s[j] not in vowels:
                j = j-1
            else:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i = i+1
                j = j-1

        return ''.join(s_list)


Approach Used: 2 pointer (easy question)

Mistakes made:
Tried to modify characters in a string in-place. However, strings in Python are immutable (i.e. we cant modify individual characters using indexing)
To solve the question, I first converted the string to a list which is mutable i.e. character swaps are allowed and then covert the list back to a string via join