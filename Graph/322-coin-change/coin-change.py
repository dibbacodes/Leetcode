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

    def tabulationHelper(self, coins, amount):
        ## Number of coins 
        n = len(coins)

        ## Initialize the dp array
        dp = [[self.INF]*(amount+1) for _ in range(n)]

        ## Base Cases
        # Fill the last row
        for target in range(amount+1):
            if target % coins[n-1] == 0:
                dp[n-1][target] = target//coins[n-1]

        ## Iterate over the array
        for index in range(n-2, -1, -1):
            for target in range(0, amount+1, 1):
                ## Calculate all possible options
                take = 1 + dp[index][target-coins[index]] if target >= coins[index] else self.INF
                not_take = 0 + dp[index+1][target] 

                ## Update dp table
                dp[index][target] = min(take, not_take)

        if dp[0][amount] >= self.INF:
            return -1
        else:
            return dp[0][amount]

    def spaceOptHelper(self, coins, amount):
        ## Number of coins 
        n = len(coins)

        ## Initialize arrays
        ahead = [self.INF for _ in range(amount+1)]
        curr = [self.INF for _ in range(amount+1)]

        ## Base Case: Assign values to last row (ahead)
        for target in range(amount+1):
            if target % coins[n-1] == 0:
                ahead[target] = target//coins[n-1]

        ## Iterate over the array
        for index in range(n-2, -1, -1):
            for target in range(0, amount+1):
                ## Calculate all possible options
                take = 1 + curr[target-coins[index]] if target >= coins[index] else self.INF
                not_take = 0 + ahead[target] 

                ## Update curr
                curr[target] = min(take, not_take)

            ahead = curr.copy()

        if ahead[amount] >= self.INF:
            return -1
        else:
            return ahead[amount]


    def coinChange(self, coins: List[int], amount: int) -> int:
        ######### MEMOIZATION ########
        
        # ## Number of coins 
        # n = len(coins)

        # ## Initialize the dp array
        # dp = [[-1]*(amount+1) for _ in range(n)]

        # ## Call helper function and return answer
        # result = self.memoHelper(0, amount, coins, dp, n)
        # return result if result != 1e9 else -1

        # ###### TABULTION ######
        # return self.tabulationHelper(coins, amount)

        ######### SPACE OPTIMIZATION #########
        return self.spaceOptHelper(coins, amount)

        