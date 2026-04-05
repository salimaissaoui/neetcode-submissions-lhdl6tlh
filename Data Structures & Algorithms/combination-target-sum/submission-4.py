class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index, target, path):
            if target < 0:
                return
            if target == 0:
                res.append(path.copy())
                return
            for i in range(index, len(nums)):
                dfs(i, target - nums[i], path + [nums[i]])
        dfs(0, target, [])
        return res