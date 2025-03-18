class Solution:
    INF = 1e9

    def memoHelper(self, row, col, matrix, nrows, ncols, dp):
        ## Base Cases
        # We reach and invalid column
        if col >= nrows or col < 0:
            return self.INF
        # We reach last row with valid column
        if row == nrows-1:
            return matrix[row][col]

        ## Return memoized reuslt if available
        if dp[row][col] != self.INF:
            return dp[row][col]

        ## Calculate all possible cases
        left = matrix[row][col] + self.memoHelper(row+1, col-1, matrix, nrows, ncols, dp)
        right = matrix[row][col] + self.memoHelper(row+1, col+1, matrix, nrows, ncols, dp)
        down = matrix[row][col] + self.memoHelper(row+1, col, matrix, nrows, ncols, dp)

        ## Memoize and return min value
        dp[row][col] = min(left, right, down)
        return dp[row][col]

    def tabulationHelper(self, matrix):
        ## Matrix Dimensions
        nrows = len(matrix)
        ncols = len(matrix[0])

        ## Initialize dp array
        dp = [[self.INF]*ncols for _ in range(nrows)]

        ## Iterate through all options
        answer = self.INF
        for row in range(nrows-1, -1, -1):
            for col in range(ncols-1, -1, -1):
                ## Base Case: Last Row
                if row == nrows-1:
                    dp[row][col] = matrix[row][col]
                    continue

                ## Calculate all possible cases
                left = matrix[row][col] + dp[row+1][col-1] if col-1 >= 0 else self.INF
                right = matrix[row][col] + dp[row+1][col+1] if col+1 < ncols else self.INF
                down = matrix[row][col] + dp[row+1][col]

                ## Update cell value in dp table
                dp[row][col] = min(left, right, down)

        return min(dp[0])

        

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ############### MEMOIZATION ###############

        # ## Matrix Dimensions
        # nrows = len(matrix)
        # ncols = len(matrix[0])

        # ## Initialize dp array
        # dp = [[self.INF]*ncols for _ in range(nrows)]

        # ## Start faling from every element of first row
        # answer = self.INF
        # for col in range(ncols):
        #     answer = min(answer, self.memoHelper(0, col, matrix, nrows, ncols, dp))

        # return answer

        ############ TABULATION ############
        return self.tabulationHelper(matrix)