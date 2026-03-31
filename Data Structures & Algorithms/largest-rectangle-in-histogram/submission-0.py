class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxarea = 0
        for i in range(n):
            j = i + 1
            k = i - 1
            h = heights[i]
            area = h
            while k >= 0 and heights[k] >= h:
                area += heights[i]
                k -= 1
            while j < n and heights[j] >= heights[i]:
                area += heights[i]
                j += 1
            if area > maxarea:
                maxarea = area
        return maxarea
