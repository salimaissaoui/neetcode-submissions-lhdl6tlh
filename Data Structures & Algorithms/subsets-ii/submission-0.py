class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        binaries = [[int(bit) for bit in format(i, f"0{len(nums)}b")] for i in range(2**len(nums))]
        print(binaries)
        res = []
        seen = set()
        for b in binaries:
            subset = []
            for x,y in zip(nums, b):
                if y != 0:
                    subset.append(x*y)
            
            if tuple(sorted(subset)) not in seen:
                res.append(subset)
            seen.add(tuple(sorted(subset)))
        return res
            
                





