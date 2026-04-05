class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1

        maxArea = 0

        while r > l:
            currentArea = min(heights[l], heights[r]) * (r-l)
            maxArea = max(maxArea, currentArea)

            if heights[l] < heights[r]:
                l+=1
                continue
            r-=1
        
        return maxArea
            



        