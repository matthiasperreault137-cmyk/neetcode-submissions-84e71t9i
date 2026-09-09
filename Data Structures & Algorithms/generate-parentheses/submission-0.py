class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        def Generation(f, b, path):
            print(f)
            if f <= 0:
                for i in range(b):
                    path += ")"
                results.append(path)
                return
            #case 1 : add opening parentheses
            f -= 1
            path += "("
            Generation(f , b , path)
            f += 1
            path = path[:-1]


            #case 2 : add closing parentheses
            if b > f:
                b -= 1
                path += ")"
                Generation(f, b, path)
                b += 1
                path = path[:-1]
            return 
        Generation(n - 1, n, "(")
        return results