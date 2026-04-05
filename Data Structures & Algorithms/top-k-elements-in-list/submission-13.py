class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        res = []

        for num in nums:
            count[num] += 1 #count each number in the list

        
        keys = []
        values = []
        for key, value in count.items():
            keys.append(key)
            values.append(value)
        
        for i in range(k):
            res.append(keys[values.index(max(values))])
            keys.pop(keys.index(keys[values.index(max(values))]))
            values.pop(values.index(max(values)))
            

        return res

        