class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # return all unique combinations of candidates where the chosen numbers sum to target
        res = []
        candidates.sort()
        def dfs(index, target, path):
            if target < 0:
                return
            if target == 0:
                res.append(path.copy())
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                dfs(i + 1, target - candidates[i], path + [candidates[i]])
        dfs(0, target, [])
        return res