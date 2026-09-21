class Solution:
    def solve(self, board: List[List[str]]) -> None:
        connected = set()
        neighbors = [(1,0), (-1,0), (0,1) , (0,-1)]
        def DFS(position):
            toVisit = [position]
            connected.add(position)
            while toVisit:
                pos = toVisit.pop()
                for neighbor in neighbors:
                    x = pos[0] + neighbor[0]
                    y = pos[1] + neighbor[1]
                    if x < 0 or x > len(board) - 1 or y < 0 or y > len(board[x]) - 1:
                        continue
                    if (x,y) in connected or board[x][y] == "X":
                        continue
                    else:
                        connected.add((x,y))
                        toVisit.append((x,y))
        for i in range(len(board)):
            if board[i][0] == "O":
                DFS((i, 0))
            if board[i][len(board[i]) - 1] == "O":
                DFS((i, len(board[i]) - 1))
        for j in range(len(board[0])):
            if board[0][j] == "O":
                DFS((0, j))
            if board[len(board) - 1][j] == "O":
                DFS((len(board) - 1, j))
        for a in range(len(board)):
            for b in range(len(board[a])):
                if (a,b) not in connected:
                    board[a][b] = "X"
        return 