class Solution:
    def isValid(self, s: str) -> bool:
        keymap = {")" : "(", "}" : "{", "]": "["}
        stack = []
        for i in range(0, len(s)):
            if s[i] in keymap:
                if stack and stack[-1] == keymap[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        return True if not stack else False