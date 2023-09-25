20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        stack.append(s[0])

        for char in s[1:]:

            if stack and ((char == ')' and stack[-1] == '(') or (char == '}' and stack[-1] == '{') or (char == ']' and stack[-1] == '[')):
                    stack.pop()
            else:
                stack.append(char)

        if len(stack) == 0:
            return True
        else:
            return False


Mistakes:
- Range error because I didn't check if stack exists but was checking top of stack
