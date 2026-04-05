class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hash1 = defaultdict(int)
        hash2 = defaultdict(int)

        for char in s:
            hash1[char] +=1
        

        for char in t:
            hash2[char] +=1

        if hash1 == hash2:
            return True
        else:
            return False







