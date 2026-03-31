class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] in row and board[i][j] != ".":
                    return False
                else:
                    row.add(board[i][j])
        for i in range(9):
            column = set()
            for j in range(9):
                if board[j][i] in column and board[j][i] != ".":
                    return False
                else:
                    column.add(board[j][i])
        for k in range(3):
            for l in range(3):
                grid = set()
                for i in range(k*3, 3 + (k * 3)):
                    for j in range(l*3, 3 + (l * 3)):
                        if board[i][j] in grid and board[i][j] != ".":
                            return False
                        else:
                            grid.add(board[i][j])
        return True