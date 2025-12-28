from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use sets to keep track of seen numbers in each row, column, and box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Ignore empty cells
                if val == '.':
                    continue
                
                # 1. Check Row
                if val in rows[r]:
                    return False
                rows[r].add(val)
                
                # 2. Check Column
                if val in cols[c]:
                    return False
                cols[c].add(val)
                
                # 3. Check 3x3 Box
                # Calculate the box index (0 to 8)
                box_idx = (r // 3) * 3 + (c // 3)
                if val in boxes[box_idx]:
                    return False
                boxes[box_idx].add(val)
                
        return True
