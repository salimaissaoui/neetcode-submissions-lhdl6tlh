from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        total = 1
        for d in digits:
            total *= len(phone_map[d])

        res = []
        for i in range(total):
            combo = []
            n = i
            for d in reversed(digits):
                letters = phone_map[d]
                combo.append(letters[n % len(letters)])
                n //= len(letters)
            res.append("".join(reversed(combo)))

        return res
