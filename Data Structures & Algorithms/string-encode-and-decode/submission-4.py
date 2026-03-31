class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        words = []
        while s:
            n = ""
            while s and s[0].isdigit():
                n += s[0]
                s = s[1:]
            num = int(n)
            s = s[1:]
            word = ""
            for i in range(num):
                word += s[i]
            words.append(word)
            s = s[num:]
        return words

                            