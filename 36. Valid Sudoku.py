class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def check_line(r: List[str]) -> bool:
            return sorted(filter(lambda x: x!='.', r)) == sorted(filter(lambda x:x!='.', set(r)))
            
        def check_each(board: List[List[str]]) -> bool:
            return all(check_line(ins) for ins in board)
            
        def check_box(board: List[List[str]]) -> bool:
                boxs = [[board[i*3+a][j*3+b] for a in range(3) for b in range(3)] for i in range(3) for j in range(3)]
                return check_each(boxs)
        row = check_each(board) 
        col =  check_each(zip(*board))
        box = check_box(board)
        result = row and col and box
        return result
    
            
