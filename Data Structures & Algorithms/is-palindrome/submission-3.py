class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i].lower() != s[j].lower():
                if s[i] == " " or s[i] == "!" or s[i] == "?" or s[i] == "," or s[i] == "'" or s[i] == "." or s[i] == ":" or s[i] == ";":
                    i += 1
                    continue
                if s[j] == " " or s[j] == "!" or s[j] == "?" or s[j] == "," or s[j] == "'" or s[j] == "." or s[j] == ":" or s[j] == ";":
                    j -= 1
                    continue
                return False
            else:
                i += 1
                j -= 1
        return True
            
