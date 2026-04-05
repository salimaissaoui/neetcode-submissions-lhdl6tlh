class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list[str])

        def freq(word):
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord('a')] +=1
            return tuple(counts)
        
        for word in strs:
            anagrams[freq(word)].append(word)
        return list(anagrams.values())
            








        