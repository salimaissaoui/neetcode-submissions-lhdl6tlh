class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0

        def expand(s, left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                    count +=1
                    left -=1
                    right +=1
            return count
        
        #odd length
        for i in range(len(s)):
            count += expand(s, i, i)
            count += expand(s, i, i+1)
        
        return count
        

        



        