class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1


        while left <= right:
            if nums[left] == target:
                return left
            
            elif nums[right] == target:
                return right
            
            else:
                left +=1
                right -=1
        
        return -1
        