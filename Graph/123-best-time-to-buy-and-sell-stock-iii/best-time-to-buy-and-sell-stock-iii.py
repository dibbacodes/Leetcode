class Solution:
    def memoHelper(self, index, canBuy, limit, prices, dp, n):
        ## Base Case
        if index == n:
            return 0

        if limit == 0:
            return 0
        
        ## Return memoized result if present
        if dp[index][canBuy][limit] != -1:
            return dp[index][canBuy][limit]

        ## Calculate all possible cases
        if canBuy:
            buy = -prices[index] + self.memoHelper(index+1, 0, limit, prices, dp, n)
            dontBuy = self.memoHelper(index+1, canBuy, limit, prices, dp, n)

            dp[index][canBuy][limit] = max(buy, dontBuy)
            return dp[index][canBuy][limit]

        else:
            sell = prices[index] + self.memoHelper(index+1, 1, limit-1, prices, dp, n)
            dontSell = self.memoHelper(index+1, 0, limit, prices, dp, n)

            dp[index][canBuy][limit] = max(sell, dontSell)
            return dp[index][canBuy][limit]
        
    def maxProfit(self, prices: List[int]) -> int:
        ####### MEMOIZATION #########

        ## Length of array
        n = len(prices)

        ## Initialize dp array
        dp = [[[-1] * 3 for _ in range(2)] for _ in range(n+1)]

        ## Call memoHelper and return answer
        return self.memoHelper(0, 1, 2, prices, dp, n)