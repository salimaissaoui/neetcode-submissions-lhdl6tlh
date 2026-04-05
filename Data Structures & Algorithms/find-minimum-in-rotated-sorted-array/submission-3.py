class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                # Pivot is in the right half
                left = mid + 1
            else:
                # Pivot is in the left half (including mid)
                right = mid
                
        
        return nums[left]