class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        #searching in rows
        for row in board:
            seen = set()
            for val in row:
                if val in seen and val != '.':
                    return False
                seen.add(val)


        #searching in coloumns
        for i in range(9):
            seen = set()
            for row in board:
                for col in row[i]:
                    if col in seen and col != '.':
                        return False
                    seen.add(col)  

        #searching for 3x3 grid
        seen1 = set()
        seen2 = set()
        seen3 = set()
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] in seen1 and board[i][j] != '.':
                    return False
                seen1.add(board[i][j])
  
            for j in range(3,6):
                if board[i][j] in seen2 and board[i][j] != '.':
                    return False 
                seen2.add(board[i][j])            

            for j in range(6,9):
                if board[i][j] in seen3 and board[i][j] != '.':
                    return False  
                seen3.add(board[i][j])           

        seen1 = set()
        seen2 = set()
        seen3 = set()
        for i in range(3,6):
            for j in range(0,3):
                if board[i][j] in seen1 and board[i][j] != '.':
                    return False
                seen1.add(board[i][j])

            for j in range(3,6):
                if board[i][j] in seen2 and board[i][j] != '.':
                    return False
                seen2.add(board[i][j])

            for j in range(6,9):
                if board[i][j] in seen3 and board[i][j] != '.':
                    return False
                seen3.add(board[i][j])

        seen1 = set()
        seen2 = set()
        seen3 = set()
        for i in range(6,9):
            for j in range(0,3):
                if board[i][j] in seen1 and board[i][j] != '.':
                    return False
                seen1.add(board[i][j])

            for j in range(3,6):
                if board[i][j] in seen2 and board[i][j] != '.':
                    return False
                seen2.add(board[i][j])

            for j in range(6,9):
                if board[i][j] in seen3 and board[i][j] != '.':
                    return False
                seen3.add(board[i][j])

        return True