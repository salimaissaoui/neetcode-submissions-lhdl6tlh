class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) -1
        while left < right:
            if s[left] == s[right]:
                left +=1
                right -=1
                continue
            elif not s[left].isalpha() and not s[left].isdigit():
                left += 1
                continue
            
            elif not s[right].isalpha() and not s[right].isdigit():
                right -= 1
                continue

            else:
                return False
        return True
        