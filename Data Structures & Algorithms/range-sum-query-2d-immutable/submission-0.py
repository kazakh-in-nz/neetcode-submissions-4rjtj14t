class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.suffix_m = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for r in range(len(matrix)):
            prefix = 0
            for c in range(len(matrix[0])):
                prefix += matrix[r][c]
                self.suffix_m[r+1][c+1] = prefix + self.suffix_m[r][c+1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        
        bottom_right = self.suffix_m[row2][col2]
        top_left = self.suffix_m[row1-1][col1-1]
        neighbour_above = self.suffix_m[row1-1][col2]
        neighbour_left = self.suffix_m[row2][col1-1]

        return bottom_right - neighbour_above - neighbour_left + top_left
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)