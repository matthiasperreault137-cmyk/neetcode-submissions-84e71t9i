class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        i = 0
        j = 0
        while i < len(heights):
            j = i
            while stack and stack[-1][1] > heights[i]:
                left, h = stack.pop()
                area = (i - left) * h
                if area > maxarea:
                    maxarea = area
                j = left
            stack.append([j, heights[i]])
            i += 1
        while stack:
            left, h = stack.pop()
            area = ((i - 1) - left + 1) * h
            if area > maxarea:
                maxarea = area
        return maxarea