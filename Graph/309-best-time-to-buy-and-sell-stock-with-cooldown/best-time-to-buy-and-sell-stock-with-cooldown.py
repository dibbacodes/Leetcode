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

    def spaceOptHelper(self, prices):
        ## Length of array
        n = len(prices)

        ## Initialize base case arrays
        ahead = [0]*(2)
        ahead2 = [0]*(2)

        ## Iterate over the array
        for index in range(n-1, -1, -1):
            curr = [0]*(2)
            for canBuy in range(1, -1, -1):
                ## Calculate all possible cases
                if canBuy:
                    buy = -prices[index] + ahead[0]
                    dontBuy = ahead[1]

                    curr[canBuy] = max(buy, dontBuy)
                else:
                    sell = prices[index] + ahead2[1]
                    dontSell = ahead[0]

                    curr[canBuy] = max(sell, dontSell)

            ahead2 = ahead.copy()
            ahead = curr.copy()

        return ahead[1]

    def maxProfit(self, prices: List[int]) -> int:
        # ####### MEMOIZATION ########

        # ## Length of prices
        # n = len(prices)

        # ## Initialize dp array
        # dp = [[-1]*(2) for _ in range(n+1)]

        # ## Call memoHelper and return answer
        # return self.memoHelper(0, 1, prices, dp, n)


        ###### SPACE OPTIMIZATION ######
        return self.spaceOptHelper(prices)