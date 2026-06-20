class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set) 
        rows = defaultdict(set) 
        squares = defaultdict(set) 
        #can also do this: rows = [set() for _ in range(9)]

        for r in range(9): 
            for c in range(9): 
                if board[r][c] == ".": 
                    continue 
                    #you're checking if the value is there other than at board[r][c]
                    #checks if it's in other rows, cols, and also it's own square
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]): 
                    return False 
                    
                cols[c].add(board[r][c]) 
                rows[r].add(board[r][c]) 
                squares[(r // 3, c // 3)].add(board[r][c]) 
        
        return True