class Solution:
    def uniqueNums(self, squares: List[str]) -> bool:
        nums = list(filter(lambda n: n != ".", squares))
        return len(nums) == len(set(nums))

    def rowValid(self, board: List[List[str]], r: int) -> bool:
        return self.uniqueNums(board[r])

    def colValid(self, board: List[List[str]], c: int) -> bool:
        return self.uniqueNums(map(lambda row: row[c], board))

    def squareValid(self, board: List[List[str]], s: int) -> bool:
        row = s // 3 * 3
        col = s % 3 * 3
        squares = []
        for i in range(3):
            squares += board[row + i][col : col + 3]
        return self.uniqueNums(squares)
    
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
                square = self.squareNum(r,c)
                if cell == ".":
                    continue
                if cell in rows[r] or cell in cols[c] or cell in squares[square]:
                    return False
                rows[r].add(cell)
                cols[c].add(cell)
                squares[square].add(cell)
        return True

