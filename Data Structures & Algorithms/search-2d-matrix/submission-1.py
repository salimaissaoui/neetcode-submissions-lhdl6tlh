class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            
            if target in range(row[0], row[-1] + 1):
                r = len(row) - 1
                l = 0
                mid = r//2

                while l <= r:
                    if row[mid] < target:
                        l = mid + 1
                        mid = (l + r) // 2
                    
                    elif row[mid] > target:
                        r = mid - 1
                        mid = (l + r) // 2
                    else:
                        return True
            
        return False
                    

                
        
        