class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row in range(len(board)):
            for col in range(len(board[row])):
                val = board[row][col]
                if val == ".":
                    continue
                row_key = (row, val)
                col_key = (val, col)
                box = (row//3,col//3,val)
                if box in seen or col_key in seen or row_key in seen:
                    return False
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box)
        return True