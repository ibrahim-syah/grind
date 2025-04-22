class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.cache = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        for r in range(rows):
            rowPrefix = 0
            for c in range(cols):
                rowPrefix += matrix[r][c]
                above = self.cache[r][c+1]
                self.cache[r+1][c+1] = rowPrefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1
        full = self.cache[r2][c2]
        above = self.cache[r1-1][c2]
        left = self.cache[r2][c1-1]
        topleft = self.cache[r1-1][c1-1]
        return full - above - left + topleft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)