class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dRow = {}
        dCol = {}
        dSq = {}
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.': continue
                if (board[i][j], i) in dRow:
                    return False
                dRow[(board[i][j], i)] = i 
                if (board[i][j], j) in dCol:
                    return False
                dCol[(board[i][j], j)] = j
                if (board[i][j], (i//3, j//3)) in dSq:
                    return False
                dSq[(board[i][j], (i//3, j//3))] = i
        return True