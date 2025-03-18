class Solution:

    INF = 1e9

    def memoHelper(self, row, col, grid, nrows, ncols, dp) -> int:
        ## Base Cases
        # When we reach the last cell: Return the cell value
        if row == nrows-1 and col == ncols-1:
            return grid[row][col]

        # Return Infinite when out of bounds
        if row >= nrows or col >= ncols:
            return self.INF

        ## Return memoized result if available
        if dp[row][col] != -1:
            return dp[row][col]

        ## Calculate all possible cases
        right = grid[row][col] + self.memoHelper(row, col+1, grid, nrows, ncols, dp)
        down = grid[row][col] + self.memoHelper(row+1, col, grid, nrows, ncols, dp)

        ## Memoize and return minimum value
        dp[row][col] = min(right, down)
        return dp[row][col]

    def tabulationHelper(self, grid):
        ## Grid dimension
        nrows = len(grid)
        ncols = len(grid[0])

        ## Initialize dp array
        dp = [[self.INF]*ncols for _ in range(nrows)]

        ## Iterate through all cells of grid
        for row in range(nrows-1, -1, -1):
            for col in range(ncols-1, -1, -1):
                # Base Case: Only one way from last cell to last cell
                if row == nrows-1 and col == ncols-1:
                    dp[row][col] = grid[row][col]
                    continue

                # Calculate all possible options
                right = grid[row][col] + dp[row][col+1] if col+1 < ncols else self.INF
                down = grid[row][col] + dp[row+1][col] if row+1 < nrows else self.INF

                # Update dp with min vale
                dp[row][col] = min(right, down)

        return dp[0][0] 


    def minPathSum(self, grid: List[List[int]]) -> int:
        ######## MEMOIZATION ########

        ## Grid dimension
        # nrows = len(grid)
        # ncols = len(grid[0])

        # ## Initialize dp array
        # dp = [[-1]*ncols for _ in range(nrows)]

        # ## Call memoHelper and return result
        # return self.memoHelper(0, 0, grid, nrows, ncols, dp)

        ######## TABULATION ########
        return self.tabulationHelper(grid)
