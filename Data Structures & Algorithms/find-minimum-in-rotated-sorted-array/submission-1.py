class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums) -1


        for i in range(len(nums)):
            if nums[-1] >= nums[i]:
                return nums[i]
            
            elif nums[i+1] < nums[i]:
                return nums[i+1]
            
            else:
                continue

       

        
            
        
       
        