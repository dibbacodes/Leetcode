class Solution:
    def memoHelper(self, index, canBuy, prices, dp, n):
        ## Base Case
        if index == n:
            return 0

        ## Return memoized result if present
        if dp[index][canBuy] != -1:
            return dp[index][canBuy]

        ## Calculate all possible cases
        if canBuy:
            buy = -prices[index] + self.memoHelper(index+1, 0, prices, dp, n)
            dontBuy = self.memoHelper(index+1, 1, prices, dp, n)

            dp[index][canBuy] = max(buy, dontBuy)
            return dp[index][canBuy]

        else:
            sell = prices[index] + self.memoHelper(index+1, 1, prices, dp, n)
            dontSell = self.memoHelper(index+1, 0, prices, dp, n)

            dp[index][canBuy] = max(sell, dontSell)
            return dp[index][canBuy]

    def tabulationHelper(self, prices):
        ## Length of array
        n = len(prices)

        ## Initialize dp array
        dp = [[0]*2 for _ in range(n+1)]

        ## Base Case
        # dp[n][canBuy] = 0

        ## Iterate over the array and update dp table
        for index in range(n-1, -1, -1):
            for canBuy in range(1, -1, -1):
                ## Calculate all possible cases
                if canBuy:
                    buy = -prices[index] + dp[index+1][0]
                    dontBuy = dp[index+1][1]

                    dp[index][canBuy] = max(buy, dontBuy)

                else:
                    sell = prices[index] + dp[index+1][1]
                    dontSell = dp[index+1][0]

                    dp[index][canBuy] = max(sell, dontSell)

        return dp[0][1]

    def maxProfit(self, prices: List[int]) -> int:
        # #### MEMOIZATION ####

        # ## Length of array
        # n = len(prices)

        # ## Initialize dp array
        # dp = [[-1]*2 for _ in range(n+1)]

        # ## Call memoHelper and return answer
        # return self.memoHelper(0, 1, prices, dp, n)

        ### TABULATION ####
        return self.tabulationHelper(prices)