class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        seen = set()

        for i in range(2**len(nums)):
            mask = format(i, f"0{len(nums)}b")
            subset = []

            for x, bit in zip(nums, mask):
                if bit == "1":
                    subset.append(x)

            key = tuple(subset)

            if key not in seen:
                res.append(subset)
                seen.add(key)

        return res