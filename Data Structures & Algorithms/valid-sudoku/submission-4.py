from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # ROWSS
        for row in board:
            rowhash = Counter(row)
            for x, v in rowhash.items():
                if x != '.' and v > 1:
                    return False

        for c in range(9):
            col = [board[r][c] for r in range(9)]
            colhash = Counter(col)

            for x, v in colhash.items():
                if x != '.' and v > 1:
                    return False

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):

                box = [board[i][j] for i in range(r, r+ 3) for j in range(c, c + 3)]
                boxhash = Counter(box)
                for x, v in boxhash.items():
                    if x != '.' and v > 1:
                        return False
        return True
