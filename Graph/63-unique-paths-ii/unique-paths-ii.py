class Solution:
    def memoHelper(self, row, col, grid, nrows, ncols, dp):
        ## Base Case
        # Return 1: When reached the end
        if row == nrows-1 and col == ncols-1:
            return 1

        # Return 0: If row or col is out of limits
        if row >= nrows or col >= ncols:
            return 0

        ## Return memoized result if available
        if dp[row][col] != -1:
            return dp[row][col]

        ## Calculate all possible cases
        right = 0
        if col+1 < ncols and not grid[row][col+1] :
            right = self.memoHelper(row, col+1, grid, nrows, ncols, dp)
        down = 0
        if row+1 < nrows and not grid[row+1][col]:
            down = self.memoHelper(row+1, col, grid, nrows, ncols, dp)

        ## Memoize and return sum
        dp[row][col] = right + down
        return dp[row][col]


        

    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        # Dimensions of grid
        nrows = len(grid)
        ncols = len(grid[0])

        # Return 0: if impossible to reach end
        if grid[nrows-1][ncols-1] == 1 or grid[0][0] == 1:
            return 0

        # Initialize dp array
        dp = [[-1]*ncols for _ in range(nrows)]

        # Call helper funtion and return answer
        return self.memoHelper(0, 0, grid, nrows, ncols, dp)