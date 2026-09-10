class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        def is_palindrome(s):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        def split(i, string, palindromes):
            if i == len(s):
                results.append(palindromes.copy())
                return
            for j in range(i, len(s)):
                letter = s[j]
                string += letter
                if is_palindrome(string):
                    palindromes.append(string)
                    split(j+1, "", palindromes)
                    palindromes.pop()

        split(0, "", [])
        return results

