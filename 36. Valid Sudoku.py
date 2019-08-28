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
    
            
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(list)
        row = defaultdict(list)
        box = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in col[i]:
                    return False
                if board[i][j] in row[j]:
                    return False
                if board[i][j] in box[i//3 + 3 * (j//3)]:
                    return False
                col[i].append(board[i][j])
                row[j].append(board[i][j])
                box[i//3 + 3 * (j//3)].append(board[i][j])
        return True
            
