class Solution:
    def memoHelper(self, index, target, dp, coins, n):
        ## Base cases
        if index == n:
            if target == 0:
                return 1
            else:
                return 0

        ## Return memoized result if available
        if dp[index][target] != -1:
            return dp[index][target]

        ## Calculate all possible cases
        take = self.memoHelper(index, target-coins[index], dp, coins, n) if target >= coins[index] else 0
        notTake = self.memoHelper(index+1, target, dp, coins, n)

        ## Memoize and return all possible answers
        dp[index][target] = take + notTake
        return dp[index][target]

    def tabulationHelper(self, amount, coins):
        ## Size of arrays coins:
        n = len(coins)

        ## Initialize the dp array
        dp = [[0]*(amount+1) for _ in range(n+1)]

        ## Base Cases
        # When no more coins are there to be taken
        dp[n][0] = 1

        ## Iterate over the array
        for index in range(n-1, -1, -1):
            for target in range(0, amount+1):
                ## Calculate all possible cases
                take = dp[index][target-coins[index]] if target >= coins[index] else 0
                notTake = dp[index+1][target]

                ## Update dp table
                dp[index][target] = take + notTake

        return dp[0][target]

    def change(self, amount: int, coins: List[int]) -> int:
        ####### MEMOIZATION ######

        # ## Size of arrays coins:
        # n = len(coins)

        # ## Initialize the dp array
        # dp = [[-1]*(amount+1) for _ in range(n)]

        # ## Call memoHelper and return answer
        # return self.memoHelper(0, amount, dp, coins, n)

        ######## TABULATION ########
        return self.tabulationHelper(amount, coins)