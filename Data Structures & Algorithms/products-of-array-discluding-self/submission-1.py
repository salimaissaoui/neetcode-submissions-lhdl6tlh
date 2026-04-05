class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        index = 0 
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j != i:
        #             res[index] *= nums[j]
            
        #     index += 1
        # return res
        count = 0 
        prefix = []
        suffix = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(prefix[i-1]*nums[i])
        
        
        for i in range(len(nums) -1, -1, -1):
            if i == len(nums) -1:
                suffix[i] = nums[i]
            else:
                suffix[i] = nums[i] * suffix[i+1]
        
        res = []
        for i in range(len(prefix)):
            if i == 0:
                res.append(suffix[i+1])
            
            elif i == len(prefix) -1:
                res.append(prefix[i-1])
            
            else:
                res.append(prefix[i-1] * suffix[i+1])
        return res




   

            

            

        