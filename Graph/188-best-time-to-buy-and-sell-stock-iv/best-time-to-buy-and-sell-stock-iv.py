class Solution:
    def spaceOptHelper(self, prices, k):
        ## Length of array
        n = len(prices)

        ## Base case array
        ahead = [[0]*(k+1) for _ in range(2)]

        ## Base cases
        # ahead[canBuy][limit] = 0
        # ahead[canBuy][0] = 0

        ## Iterate over the prices array
        for index in range(n-1, -1, -1):
            # Curr array initialization
            curr = [[0]* (k+1) for _ in range(2)]
            for canBuy in range(1, -1, -1):
                for limit in range(k, 0, -1):
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
            
        return ahead[1][k]

    def maxProfit(self, k: int, prices: List[int]) -> int:
        return self.spaceOptHelper(prices, k)