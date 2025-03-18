class Solution:
    INF = 1e9
    def memoHelper(self, row, col, triangle, dp, nrows):
        ## Base Cases
        if row == nrows-1:
            return triangle[row][col]

        ## Return memoized result if available
        if dp[row][col] != -1:
            return dp[row][col]

        ## Calculate all possible cases
        down = triangle[row][col] + self.memoHelper(row+1, col, triangle, dp, nrows)
        up = triangle[row][col] + self.memoHelper(row+1, col+1, triangle, dp, nrows)
        
        ## Memoize and return answer
        dp[row][col] = min(down, up)
        return dp[row][col]

    def tabulationHelper(self, triangle):
        ## Triangle Dimensions
        nrows = len(triangle)

        ## Initialize dp array
        dp = [[self.INF]*nrows for _ in range(nrows)]

        ## Iterate through all possible options
        for row in range(nrows-1, -1, -1):
            for col in range(row, -1, -1):
                # Base Case: Last Row
                if row == nrows-1:
                    dp[row][col] = triangle[row][col]
                    continue

                # Calculate all possible cases
                down = triangle[row][col] + dp[row+1][col]
                up = triangle[row][col] + dp[row+1][col+1]
        
                # Update dp cell with min value
                dp[row][col] = min(down, up)

        return dp[row][col]


    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # ########## MEMOIZATION #############
        # ## Triangle Dimensions
        # nrows = len(triangle)

        # ## Initialize dp array
        # dp = [[-1]*nrows for _ in range(nrows)]

        # ## Call memoHelper and return answer
        # return self.memoHelper(0, 0, triangle, dp, nrows)

        ########## TABULATION ##########
        return self.tabulationHelper(triangle)