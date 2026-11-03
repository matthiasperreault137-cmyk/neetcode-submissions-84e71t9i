class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        movements = [(1, 0), (0, 1)]
        dp = {}
        def PathSum(node):
            if node == (m-1 ,n -1):
                print("node : " + str(node[0]) + str(node[1]) + str(1))
                return 1
            total = 0
            for mov in movements:
                x = node[0] + mov[0]
                y = node[1] + mov[1]
                if x < 0 or y < 0 or x >= m or y >= n:
                    continue
                if (x, y) in dp:
                    total += dp[(x,y)]
                    continue
                total += PathSum((x,y))
            dp[node] = total
            print("node : " + str(node[0]) + str(node[1]) + "total : " + str(total))
            return total
        return PathSum((0,0))
                
            