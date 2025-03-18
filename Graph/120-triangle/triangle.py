class Solution:
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

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ########## MEMOIZATION #############
        ## Triangle Dimensions
        nrows = len(triangle)

        ## Initialize dp array
        dp = [[-1]*nrows for _ in range(nrows)]

        ## Call memoHelper and return answer
        return self.memoHelper(0, 0, triangle, dp, nrows)