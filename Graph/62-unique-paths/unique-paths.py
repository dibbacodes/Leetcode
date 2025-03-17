class Solution:
    def memoHelper(self, row, col, m, n, dp):
        ## Base Cases

        # Return 1: if reached the destination
        if row == m-1 and col == n-1:
            return 1
        
        # Return 0: if row or col is beyond limit
        if row >= m or col >= n:
            return 0

        ## Return memoized results if available
        if dp[row][col] != -1:
            return dp[row][col]

        ## Calculate all possible options
        right = self.memoHelper(row, col+1, m, n, dp)
        down = self.memoHelper(row+1, col, m, n, dp)

        ## Memoize and return the sum
        dp[row][col] = right + down
        return dp[row][col]

    def uniquePaths(self, m: int, n: int) -> int:
        #### MEMOIZATION ####

        # Initialize dp array
        dp = [[-1]*n for _ in range(m)]

        # Call helper function and return the answer
        return self.memoHelper(0, 0, m, n, dp)