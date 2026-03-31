class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fuckyou = {}
        answer = []
        for i in range(len(strs)):
            s = strs[i]
            anagram = self.anagram(s)
            if anagram in fuckyou:
                fuckyou[anagram].append(s)
            else:
                fuckyou[anagram] = [s]
        for anagram in fuckyou:
            answer.append(fuckyou[anagram])
        return answer


    def anagram(self, s):
        array = [0] * 26
        for char in s:
            array[ord(char) - ord('a')] += 1
        return tuple(array)
