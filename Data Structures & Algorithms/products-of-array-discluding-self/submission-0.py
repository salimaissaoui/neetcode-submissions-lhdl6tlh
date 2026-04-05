class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        index = 0 
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    res[index] *= nums[j]
            
            index += 1
        return res
            

        