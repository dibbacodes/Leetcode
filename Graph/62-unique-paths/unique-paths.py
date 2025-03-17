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

    def tabulationHelper(self, m, n):
        # Initialize dp array
        dp = [[0]*n for _ in range(m)]

        # Base Cases
        dp[m-1][n-1] = 1 # One way to reach from end to end

        # Iterate through all cases
        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                # If last cell: Skip
                if row == m-1 and col == n-1:
                    continue
                
                # left
                left = 0
                if col+1 < n:
                    left = dp[row][col+1]
                
                # right
                up = 0
                if row+1 < m:
                    up = dp[row+1][col]

                dp[row][col] = left + up

        return dp[0][0]

    def spaceOptHelper(self, m, n) -> int:
        # Initialize required arrays
        curr = [0]*n
        next = [0]*n
        
        # Base Cases
        next[n-1] = 1 # One way to reach from end to end

        # Iterate through all cases
        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):

                # If last cell: Skip
                if row == m-1 and col == n-1:
                    curr[col] = 1
                    continue
                
                # left
                left = 0
                if col+1 < n:
                    left = curr[col+1]
                
                # right
                up = 0
                if row+1 < m:
                    up = next[col]

                curr[col] = left + up
            
            next = curr

        return next[0]

    def uniquePaths(self, m: int, n: int) -> int:
        #### MEMOIZATION ####

        # # Initialize dp array
        # dp = [[-1]*n for _ in range(m)]

        # # Call helper function and return the answer
        # return self.memoHelper(0, 0, m, n, dp)

        ##### TABULATION #####
        # return self.tabulationHelper(m, n)

        ##### SPACE OPTIMIZATION #####
        return self.spaceOptHelper(m, n)

