class Solution:

    def encode(self, strs: List[str]) -> str:
        intermediate = ""
        result = ""
        for s in strs:
            intermediate += str(len(s)) + "#" + s
        for char in intermediate:
            result += chr(ord(char) + 23)
        return result

    def decode(self, string: str) -> List[str]:
        words = []
        s = ""
        for char in string:
            s += chr(ord(char) - 23)
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

                            