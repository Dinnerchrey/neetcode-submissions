class Solution:
    def squareNum(self, r, c):
        return (r // 3) * 3 + (c // 3)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = dict()
        cols = dict()
        squares = dict()

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == ".":
                    continue
                square = (r // 3) * 3 + (c // 3)
                if cell in rows[r] or cell in cols[c] or cell in squares[square]:
                    return False

                rows[r].add(cell)
                cols[c].add(cell)
                squares[square].add(cell)
        return True
