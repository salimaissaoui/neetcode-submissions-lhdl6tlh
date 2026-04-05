class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(index, subset):
            if index == len(nums):
                result.append(subset.copy())
                return
            
            dfs(index + 1, subset)
            dfs(index + 1, subset + [nums[index]])
        dfs(0, [])
        return result
        