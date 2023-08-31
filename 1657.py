1657. Determine if Two Strings Are Close

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.


Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"


Solution:

Created this based on test cases and brute forced it, there will be a better and more concise solution for this.

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False
        
        hash_word1 = {}
        hash_word2 = {}

        for char in word1:
            if char not in hash_word1:
                hash_word1[char] = 1
            else:
                hash_word1[char] += 1

        for char in word2:
            if char not in hash_word2:
                hash_word2[char] = 1
            else:
                hash_word2[char] += 1   

        for char in hash_word2:
            if char not in hash_word1:
                return False

        for char in hash_word1:
            if char not in hash_word2:
                return False       

        sorted_list1 = sorted(list(hash_word1.values()))
        sorted_list2 = sorted(list(hash_word2.values()))

        if sorted_list1 == sorted_list2:
            return True
        else:
            return False                                                                                                       
                                                                                                      
