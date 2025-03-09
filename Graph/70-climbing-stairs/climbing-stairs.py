class Solution:
    def climb(self, index: int, n: int, dp) -> int:
        # base cases
        if index == n: # if we reach the top
            return 1

        if index > n: # if index goes beyond the top
            return 0

        # Memoization
        if dp[index] != -1:
            return dp[index]

        # Recursion cases
        one_step = self.climb(index + 1, n, dp)
        two_step = self.climb(index + 2, n, dp)

        # Return the total
        dp[index] = one_step + two_step
        return dp[index]

    def climbStairs(self, n: int) -> int:
        # Initialise dp array
        dp = [-1 for _ in range(n)]

        answer = self.climb(0, n, dp)
        return answer
