class Solution:
    def uniqueNums(self, squares: List[str]) -> bool:
        nums = list(filter(lambda n: n != ".", squares))
        return len(nums) == len(set(nums))

    def rowValid(self, board: List[List[str]], r: int) -> bool:
        return self.uniqueNums(board[r])

    def colValid(self, board: List[List[str]], c: int) -> bool:
        return self.uniqueNums(map(lambda row : row[c], board))
    
    def squareValid(self, board: List[List[str]], i: int) -> bool:
        row = i // 3 * 3
        col = i % 3 * 3 
        squares = []
        for i in range(3):
            squares += board[row + i][col : col + 3]
        return self.uniqueNums(squares)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not (self.rowValid(board, i) and self.colValid(board, i) and self.squareValid(board, i)):
                return False
        return True
                
