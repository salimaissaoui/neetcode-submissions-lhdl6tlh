from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        l = 0
        longest = 0

        for r in range(len(s)):
            seen[s[r]] += 1

            while seen[s[r]] > 1:
                seen[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest

    

            