class Solution:
    def memoHelper(self, index, canBuy, prices, dp, n, fee):
        ## Base case
        if index == n:
            return 0

        ## Return memoized result if present
        if dp[index][canBuy] != -1:
            return dp[index][canBuy]

        ## Calculate all cases
        if canBuy:
            buy = -prices[index] + self.memoHelper(index+1, 0, prices, dp, n, fee)
            dontBuy = self.memoHelper(index+1, 1, prices, dp, n, fee)

            dp[index][canBuy] = max(buy, dontBuy)

        else:
            sell = prices[index]-fee + self.memoHelper(index+1, 1, prices, dp, n, fee)
            dontSell = self.memoHelper(index+1, 0, prices, dp, n, fee)

            dp[index][canBuy] = max(sell, dontSell)

        ## Return
        return dp[index][canBuy]

    def maxProfit(self, prices: List[int], fee: int) -> int:
       ## Length of array
       n = len(prices)

       ## Initialize dp array
       dp = [[-1]*2 for _ in range(n+1)] 

       ## Call memoHelper and return answer
       return self.memoHelper(0, 1, prices, dp, n, fee)