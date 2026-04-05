class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        maxArea = 0
        for i, rect in enumerate(heights):
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                area = height * width
                maxArea = max(maxArea, area)
            stack.append(i)

        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            area = height * width
            maxArea = max(maxArea, area)

        return maxArea