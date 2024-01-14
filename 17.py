Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Solution:
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        answer = []
        data_dict = { 2: ["a", "b", "c"],
                      3: ["d", "e", "f"], 
                      4: ["g", "h", "i"],
                      5: ["j", "k", "l"],
                      6: ["m", "n", "o"],
                      7: ["p", "q", "r", "s"],
                      8: ["t", "u", "v"],
                      9: ["w", "x", "y", "z"]
        }

        for number in digits:
            if int(number) > 1 and int(number) <=9:
                if answer:
                    new_answer = []
                    for str_1 in answer:
                        for str_2 in data_dict[int(number)]:
                            new_answer.append(''.join((str_1,str_2)))
                    answer = new_answer
                else:
                    for str_2 in data_dict[int(number)]:
                        answer.append(str_2)
        
        return answer
