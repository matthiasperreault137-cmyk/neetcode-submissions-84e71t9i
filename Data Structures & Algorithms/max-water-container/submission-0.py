class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return None
        i = 0 
        j  = len(heights) - 1
        maxarea = 0
        while i < j:
            minh = None
            if heights[i] <= heights[j]:
                minh = heights[i]
            else:
                minh = heights[j]     
            width = (j - i)
            area = minh * width
            if area > maxarea:
                maxarea = area
            elif minh == heights[i]:
                i += 1
            else:
                j -= 1
        return maxarea
