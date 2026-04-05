from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""


        freq = Counter(t)
        chars = {}



        l, r, minwindow, count = 0, 0, float("inf"), 0

        for r in range(len(s)):
            char = s[r]
            chars[char] = chars.get(char,0) + 1

            if char in freq and chars[char] == freq[char]:
                count+=1

            while count == len(freq):

                if r - l + 1 < minwindow:
                    minwindow = r - l + 1
                    start = l
                
                charleft = s[l]
                chars[charleft] -=1

                if charleft in freq and chars[charleft] < freq[charleft]:
                    count-=1
                l +=1
        return s[start:start + minwindow] if minwindow != float("inf") else ""




        



        