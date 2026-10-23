class Solution:
    def squareNum(self, r, c):
        return (r // 3) * 3 + (c // 3)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = dict()
        cols = dict()
        squares = dict()

        for i in range(9):
            rows[i] = set()
            cols[i] = set()
            squares[i] = set()

        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == ".":
                    continue
                square = self.squareNum(r, c)
                if cell in rows[r] or cell in cols[c] or cell in squares[square]:
                    return False
                rows[r].add(cell)
                cols[c].add(cell)
                squares[square].add(cell)
        return True
