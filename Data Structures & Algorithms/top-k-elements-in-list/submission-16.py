from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        top_k = [item for item, _ in counter.most_common(k)]

        return top_k