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

    def tabulationHelper(self, prices):
        ## Length of array
        n = len(prices)

        ## Initialize dp array
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n+1)]

        ## Base Cases
        # dp[n][canBuy][limit] = 0
        # dp[index][canBuy][0] = 0

        ## Iterate over the array
        for index in range (n-1, -1, -1):
            for canBuy in range(1, -1, -1):
                for limit in range(2, 0, -1):
                    ## Calculate all possible cases
                    if canBuy:
                        buy = -prices[index] + dp[index+1][0][limit]
                        dontBuy = dp[index+1][canBuy][limit]

                        dp[index][canBuy][limit] = max(buy, dontBuy)

                    else:
                        sell = prices[index] + dp[index+1][1][limit-1]
                        dontSell = dp[index+1][0][limit]

                        dp[index][canBuy][limit] = max(sell, dontSell)
            
        return dp[0][1][2]

    def spaceOptHelper(self, prices):
        ## Length of array
        n = len(prices)

        ## Base case array
        ahead = [[0]*3 for _ in range(2)]

        ## Base cases
        # ahead[canBuy][limit] = 0
        # ahead[canBuy][0] = 0

        ## Iterate over the prices array
        for index in range(n-1, -1, -1):
            # Curr array initialization
            curr = [[0]*3 for _ in range(2)]
            for canBuy in range(1, -1, -1):
                for limit in range(2, 0, -1):
                    ## Calculate all possible cases
                    if canBuy:
                        buy = -prices[index] + ahead[0][limit]
                        dontBuy = ahead[canBuy][limit]

                        curr[canBuy][limit] = max(buy, dontBuy)

                    else:
                        sell = prices[index] + ahead[1][limit-1]
                        dontSell = ahead[0][limit]

                        curr[canBuy][limit] = max(sell, dontSell)

            ahead = curr.copy()
            
        return ahead[1][2]
        
    def maxProfit(self, prices: List[int]) -> int:
        ####### MEMOIZATION #########

        ## Length of array
        # n = len(prices)

        # ## Initialize dp array
        # dp = [[[-1] * 3 for _ in range(2)] for _ in range(n+1)]

        # ## Call memoHelper and return answer
        # return self.memoHelper(0, 1, 2, prices, dp, n)

        ###### TABULATION ######
        # return self.tabulationHelper(prices)

        ###### SPACE OPTIMIZATION #######
        return self.spaceOptHelper(prices)

    