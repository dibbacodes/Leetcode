class Solution:
    INF = 1e9
    def memoHelper(self, index, target, coins, dp, n):
        ## Base Case
        # No more coins needed when target is 0
        if target == 0:
            return 0
        # Can't take anymore coins
        if index == n:
            return self.INF

        ## Return memoized result if possible
        if dp[index][target] != -1:
            return dp[index][target]

        ## Calculate all possible options
        take = 1 + self.memoHelper(index, target-coins[index], coins, dp, n) if target >= coins[index] else self.INF
        not_take = 0 + self.memoHelper(index+1, target, coins, dp, n)

        ## Return minimum value
        dp[index][target] = min(take, not_take)
        return dp[index][target]

    def coinChange(self, coins: List[int], amount: int) -> int:
        ######### MEMOIZATION ########
        
        ## Number of coins 
        n = len(coins)

        ## Initialize the dp array
        dp = [[-1]*(amount+1) for _ in range(n)]

        ## Call helper function and return answer
        result = self.memoHelper(0, amount, coins, dp, n)
        return result if result != 1e9 else -1

        