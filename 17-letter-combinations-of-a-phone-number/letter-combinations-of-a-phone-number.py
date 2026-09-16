class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
            
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        current = ""

        def backtrack(index):
            nonlocal current

            if index == len(digits):
                result.append(current)
                return

            letters = phone[digits[index]]

            for letter in letters:
                current += letter
                backtrack(index + 1)
                current = current[:-1]

        backtrack(0)
        return result