class Solution:
    def memoHelper(self, index, canBuy, prices, dp, n):
        ## Base case
        if index >= n:
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
            sell = prices[index] + self.memoHelper(index+2, 1, prices, dp, n)
            dontSell = self.memoHelper(index+1, 0, prices, dp, n)

            dp[index][canBuy] = max(sell, dontSell)
            return dp[index][canBuy]

    def maxProfit(self, prices: List[int]) -> int:
        ####### MEMOIZATION ########

        ## Length of prices
        n = len(prices)

        ## Initialize dp array
        dp = [[-1]*(2) for _ in range(n+1)]

        ## Call memoHelper and return answer
        return self.memoHelper(0, 1, prices, dp, n)