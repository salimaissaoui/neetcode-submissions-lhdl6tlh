class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = len(nums) //2

        while index >= 0 or index <len(nums):
            if nums[index] > target:
                if index != 0 and nums[index-1] >=target:
                    index -=1
                else:
                    return -1
            
            elif nums[index] < target:
                if index != len(nums)-1 and  nums[index +1] <= target:
                    index +=1
                else:
                    return -1
                
            
            else:
                return index
        return -1


        