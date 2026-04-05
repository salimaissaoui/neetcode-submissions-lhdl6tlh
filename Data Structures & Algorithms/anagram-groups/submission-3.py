from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []

        groups = defaultdict(list)

        for word in strs:
            key = tuple(sorted(Counter(word).items()))
            groups[key].append(word)
        
        return list(groups.values())
