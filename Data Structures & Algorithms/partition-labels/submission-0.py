class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        seen = {}
        results = []
        for i in range(len(s)):
            char = s[i]
            if char in seen:
                j = i
                while j > seen[char]:
                    j -= results.pop()
                results.append(i - j + 1)
            else:
                results.append(1)
            seen[char] = i
        return results