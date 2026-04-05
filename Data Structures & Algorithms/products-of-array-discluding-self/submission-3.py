class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        anythingButSelf = {
            i: [nums[j] for j in range(len(nums)) if j != i]
            for i in range(len(nums))
        }

        res = []
        for l in anythingButSelf.values():
            res.append(math.prod(l))
        
        return res