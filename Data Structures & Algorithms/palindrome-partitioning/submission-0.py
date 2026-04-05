from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(s):
            l = 0
            r = len(s) - 1

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        def backtrack(start, partition):
            if start >= len(s):
                res.append(partition)
                return
            for end in range(start, len(s)):
                if isPalindrome(s[start:end + 1]):
                    backtrack(end + 1, partition + [s[start:end + 1]])
        backtrack(0, [])
        return res
            
            

