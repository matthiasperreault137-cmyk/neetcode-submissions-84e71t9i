class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        reverse = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " " or s[i] == "!" or s[i] == "?" or s[i] == "," or s[i] == "'" or s[i] == "." or s[i] == ":" or s[i] == ";":
                continue
            else:
                reverse = reverse + s[i].lower()
        for i in range(len(s)):
            if s[i] == " " or s[i] == "!" or s[i] == "?" or s[i] == "," or s[i] == "'" or s[i] == "." or s[i] == ":" or s[i] == ";":
                continue
            else:
                clean = clean + s[i].lower()
        if clean == reverse:
            return True
        else:
            return False