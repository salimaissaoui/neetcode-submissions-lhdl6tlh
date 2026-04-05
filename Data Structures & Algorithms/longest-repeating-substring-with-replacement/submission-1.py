from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)  # Keep track of letter counts in the window
        max_count = 0  # The count of the most frequent letter in the current window
        l = 0  # Left pointer for the sliding window
        res = 0  # The result, maximum length of the substring
        
        for r in range(len(s)):  # r is the right pointer
            count[s[r]] += 1
            max_count = max(max_count, count[s[r]])  # Update the most frequent letter count
            
            # If the number of changes required (window size - max_count) is more than k, shrink the window
            while (r - l + 1) - max_count > k:
                count[s[l]] -= 1
                l += 1
            
            # Update the result with the current window size
            res = max(res, r - l + 1)
        
        return res
