class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        #searching in rows
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] in seen and board[i][j] != '.':
                    return False
                seen.add(board[i][j])


        #searching in coloumns
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] in seen and board[j][i] != '.':
                        return False
                seen.add(board[j][i])  

        #searching for 3x3 grid
        for r in range(0,9,3):
            for c in range(0,9,3):
                seen = set()
                for i in range(r,r+3):
                    for j in range(c,c+3):
                        if board[i][j] in seen and board[i][j] != '.':
                            return False
                        seen.add(board[i][j])

        return True