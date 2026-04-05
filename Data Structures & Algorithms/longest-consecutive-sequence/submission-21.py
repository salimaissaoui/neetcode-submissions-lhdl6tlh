class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        sequences = []

        if not nums:
            return 0
        for num in nums:
            seq = [num]
            next_num = num + 1
            while next_num in num_set:
                seq.append(next_num)
                next_num += 1
            if len(seq) > 1:  # only consider sequences of length >= 2
                sequences.append(seq)
        
        if sequences:
            longest = max(sequences, key=len)
            return len(longest)
        
        return 1