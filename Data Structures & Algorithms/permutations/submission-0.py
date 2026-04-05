class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #use backtracking to generate all permutations of the given list
        result = []
        def backtrack(start, end):
            if start == end:
                return result.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1, end)
                nums[start], nums[i] = nums[i], nums[start]
        backtrack(0, len(nums))
        return result