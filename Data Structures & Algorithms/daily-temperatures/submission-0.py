class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monostack = []
        results = [0] * len(temperatures)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            if not monostack:
                monostack.append([temp, i])
                continue
            while monostack and temp > monostack[-1][0]:
                    stackt, stacki = monostack.pop()
                    results[stacki] = i - stacki
            monostack.append([temp, i])
        return results

