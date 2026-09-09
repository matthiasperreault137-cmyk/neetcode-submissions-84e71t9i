class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = ""

        def DFS(i, position, path, used):
            r, c = position
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False
            letter = board[r][c]
            if letter != word[i]:
                return False
            path += letter
            if path == word:
                return True
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # up, down, left, right
                newPos = (r + dr, c + dc)
                if newPos in used:
                    continue
                used.add(newPos)
                if DFS(i + 1, newPos, path, used):
                    return True
                used.remove(newPos)
            path = path[:-1]
            return False
            
        used = set()

        for i in range(len(board)):
            for j in range(len(board[i])):
                position = (i , j)
                if position in used:
                    continue
                used.add(position)
                if DFS(0, position, path, used):
                    return True
                used.remove(position)

        return False