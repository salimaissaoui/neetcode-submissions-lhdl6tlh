class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge_sorted(A, B):
            i, j = 0, 0
            result = []
            
            while i < len(A) and j < len(B):
                if A[i] <= B[j]:
                    result.append(A[i])
                    i += 1
                else:
                    result.append(B[j])
                    j += 1
            
            # Add remaining elements
            result.extend(A[i:])
            result.extend(B[j:])
    
            return result
        def find_median(nums):
            n = len(nums)
            if n % 2 == 0:
                # Even length: average of two middle elements
                mid1 = nums[n // 2 - 1]
                mid2 = nums[n // 2]
                median = (mid1 + mid2) / 2
            else:
                # Odd length: single middle element
                median = nums[n // 2]
            return median
        

        nums = merge_sorted(nums1, nums2)
        return find_median(nums)