from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1  # count each number in the list

        keys = []
        values = []
        for key, value in count.items():
            keys.append(key)
            values.append(value)
        
        res = []
        for i in range(k):
            # Find the max frequency once per iteration
            max_val = max(values)
            max_idx = values.index(max_val)
            
            # Use max_idx to append the key and remove from both lists
            res.append(keys[max_idx])
            keys.pop(max_idx)
            values.pop(max_idx)
        
        return res
