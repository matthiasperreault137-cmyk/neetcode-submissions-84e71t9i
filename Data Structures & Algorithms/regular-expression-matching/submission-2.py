class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        for i in range(len(s) + 1):
            for j in range(len(p) + 1):
                dp[(i,j)] = False
        dp[(len(s), len(p))] = True
        a = len(s)
        b = len(p) - 1
        while a >= 0:
            b = len(p) - 1
            while b >= 0:
                star = False
                char2 = p[b]
                if char2 == "*":
                    b -= 1
                    star = True
                    char2 = p[b]
                if a == len(s):
                    if star == True:
                        dp[(a,b)] = dp[(a,b + 2)]
                    else:
                        dp[(a,b)] = False
                    b -= 1
                    continue
                char1 = s[a]
                if star:
                    if char1 == char2:
                        if dp[(a + 1,b)] == True or dp[(a, b + 2)] == True or dp[(a + 1, b + 2)] == True:
                            dp[(a, b)] = True
                        else:
                            dp[(a,b)] = False
                    else:
                        if char2 == ".":
                            if dp[(a + 1,b)] == True or dp[(a, b + 2)] == True or dp[(a + 1, b + 2)] == True:
                                dp[(a, b)] = True
                            else:
                                dp[(a,b)] = False
                        else:
                            if dp[(a, b + 2)] == True:
                                dp[(a, b)] = True
                            else:
                                dp[(a, b)] = False
                else:
                    if char1 != char2:
                        if char2 == ".":
                            if dp[(a + 1, b + 1)] == True:
                                dp[(a, b)] = True
                            else:
                                dp[(a, b)] = False
                        else:
                            dp[(a, b)] = False
                    else:    
                        if dp[(a + 1, b + 1)] == True:
                            dp[(a, b)] = True
                        else:
                            dp[(a, b)] = False
                b -= 1
            a -= 1
        return dp[(0,0)]