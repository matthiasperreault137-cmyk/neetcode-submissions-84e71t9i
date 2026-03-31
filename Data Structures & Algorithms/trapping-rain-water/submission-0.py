class Solution:
    def trap(self, height: List[int]) -> int:
        maxleftstack = []
        maxrightstack = []
        maxleft = 0
        maxright = 0
        total = 0
        for i in range(len(height)):
            maxleftstack.append(maxleft)
            if height[i] > maxleft:
                maxleft = height[i]
        for i in range(len(height)-1, -1, -1):
            maxrightstack.append(maxright)
            if height[i] > maxright:
                maxright = height[i]
        for i in range(len(height)):
            minh = min(maxleftstack[i], maxrightstack[len(height) - 1 - i])
            water = minh - height[i]
            if water < 0:
                water = 0
            total += water
        return total

            