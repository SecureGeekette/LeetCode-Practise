205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Solution:

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashmap = {}
        for i in range(len(s)):
            if t[i] not in hashmap.values():
                if s[i] not in hashmap:
                    hashmap[s[i]] = t[i]
                else:
                    if hashmap[s[i]] != t[i]:
                        return False
            else:
                for k, v in hashmap.items():
                    if v == t[i]:
                        if k != s[i]:
                            return False
        
        return True


Optimized solution with Zipped Set

why using zip ?
=> zip function would pair the first item of first iterator (i.e s here) to the first item of second iterator (i.e t here). set() would remove duplicate items from the zipped tuple. It is like the first item of first iterator mapped to the first item of second iterator as it would in case of a hashtable or dictionary.
Understand using examples:

# when strings ae isomorphic:
s = "egg"
t = "add"

zipped_set = {('e', 'a'), ('g', 'd')}
# now comparing their lengths when duplicacies are removed
return len(zipped_set) == len(set(s)) == len(set(d))
# return 2 == 2 == 2 -> True
# when strings are not isomorphic:
s = "egk"
t = "add"

zipped_set = {('e', 'a'), ('g', 'd'), ('k', 'd')}
# now comparing their lengths when duplicacies are removed
return len(zipped_set) == len(set(s)) == len(set(d))

# return 3 == 3 == 2 -> False

    def isIsomorphic(self, s: str, t: str) -> bool:

        zipped_set = set(zip(s, t))
        
        if len(zipped_set) == len(set(s)) == len(set(t)):
            return True
        else:
            return False

