from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count occurrences
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        # 2. Convert the frequencies to a list
        occurrences = list(count.values())

        # 3. For each of the k highest frequencies:
        res = []
        for _ in range(k):
            # a) Find the max frequency
            max_val = max(occurrences)
            # b) Find the number with this frequency
            for key, val in count.items():
                if val == max_val:
                    res.append(key)
                    # c) Remove this frequency from the list
                    occurrences.remove(max_val)
                    # d) Remove the key from the dictionary
                    del count[key]
                    break  # Important to stop once we've handled one key with this frequency

        return res
