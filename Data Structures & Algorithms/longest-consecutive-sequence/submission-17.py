from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Handle empty input

        num_set = set(nums)  # Convert to a set for O(1) lookups
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:  # Start of a sequence
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:  # Expand the sequence
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest
