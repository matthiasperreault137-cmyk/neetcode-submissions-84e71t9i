class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        results = []
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def search(i, string):
            digit = digits[i]
            letters = digit_map[digit]
            for j in range(len(letters)):
                letter = letters[j]
                string += letter
                if i + 1 == len(digits):
                    results.append(string)
                else:
                    search(i + 1, string)
                string = string[:-1]
            return  results
        search(0,"")
        return results