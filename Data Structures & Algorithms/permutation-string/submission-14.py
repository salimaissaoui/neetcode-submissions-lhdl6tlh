class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l, r = 0, len(s1) - 1
        Cs1 = Counter(s1)
        Cs2 = Counter(s2[0:r + 1])
        while r < len(s2) - 1:
            if Cs1 == Cs2:
                return True
            
            Cs2[s2[l]] -= 1
            l += 1
            r += 1
            Cs2[s2[r]] += 1
        
        if Cs1 == Cs2:
             return True
        return False



            