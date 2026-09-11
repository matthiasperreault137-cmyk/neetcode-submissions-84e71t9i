class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        board = []
        diags1 = set()
        diags2 = set()
        rows = set()
        cols = set()
        def checkValidity(row, col):
            if col in cols:
                return False
            if row in rows:
                return False
            if row - col in diags1 or row + col in diags2:
                return False
            return True
        def addNewPos(row, col):
            rows.add(row)
            cols.add(col)
            diags1.add(row - col)
            diags2.add(row + col)
        def removePos(row,col):
            rows.remove(row)
            cols.remove(col)
            diags1.remove(row - col)
            diags2.remove(row + col)
        def placeQueen(col):
            string = ""
            for i in range(n):
                if i == col:
                    string += "Q"
                    continue
                string += "."
            return string
        def queenRecurse(i, board):
            if i == n:
                results.append(board.copy())
                return 
            for j in range(n):
                if checkValidity(i, j):
                    string = placeQueen(j)
                    addNewPos(i, j)
                    board.append(string)
                    queenRecurse(i + 1, board)
                    board.pop()
                    removePos(i, j)
            return
        queenRecurse(0, board)
        return results

