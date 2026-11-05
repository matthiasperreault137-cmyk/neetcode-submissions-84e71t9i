class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)
        for i in range(len(temperatures)):
            t = temperatures[i]
            if not stack:
                stack.append((i, t))
                continue
            elif stack[-1][1] >= t:
                stack.append((i,t))
                continue
            while stack and stack[-1][1] < t:
                popVal = stack.pop()
                results[popVal[0]] = i - popVal[0]
            stack.append((i,t))
        return results
     
                