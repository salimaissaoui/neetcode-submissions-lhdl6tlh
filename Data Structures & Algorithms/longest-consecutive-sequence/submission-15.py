class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = []
        count = 1
        if len(nums) == 0:
            return 0
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        for index in range(len(nums)):
            if nums[index - 1] == nums[index] - 1 and index != 0:
                count+=1
                res.append(count)
            elif len(nums) == 1:
                return 1
            else:
                count = 1
            
            
            

            
        
      

        return max(res)
         
                

        