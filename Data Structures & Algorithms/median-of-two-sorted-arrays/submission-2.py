class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        total = len(A) + len(B)
        half = total // 2
        left = 0
        right = len(A) - 1

        while True:
            i = (left + right) // 2
            # i is the index of the middle element of the first array
            j = half - i - 2
            # j is the index of the middle element of the second array, subtracting the index of the middle element of the first array and subtracting 2
            # Aleft is the left element of the first array, if i is negative, then it is negative infinity
            Aleft = A[i] if i >= 0 else float("-infinity")
            # Aright is the right element of the first array, if i is the last index of the array, then it is infinity
            Aright = A[i+1] if i+1 < len(A) else float("infinity")
            # Bleft is the left element of the second array, if j is negative, then it is negative infinity
            Bleft = B[j] if j >= 0 else float("-infinity")
            # Bright is the right element of the second array, if j is the last index of the array, then it is infinity
            Bright = B[j+1] if j+1 < len(B) else float("infinity")
            # if the left elements of both arrays are less than the right elements of the other array, then we have found the median
            if Aleft <= Bright and Bleft <= Aright:
                # if the total number of elements is even, then the median is the average of the two middle elements
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                # if the total number of elements is odd, then the median is the middle element of the larger array
                else:
                    return min(Aright, Bright)
            # if the left element of the first array is greater than the right element of the second array, then we need to move the left pointer to the left
            elif Aleft > Bright:
                right= i - 1
            # if the left element of the second array is greater than the right element of the first array, then we need to move the left pointer to the right
            else:
                left = i + 1
            
            
    
    
    
    
    
    
    
    