from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        seen = defaultdict(int)
        max_freq = 0

        for r in range(len(s)):
            seen[s[r]] += 1
            max_freq = max(max_freq, seen[s[r]])

            # window size - most frequent char count > k → shrink
            while (r - l + 1) - max_freq > k:
                seen[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest
