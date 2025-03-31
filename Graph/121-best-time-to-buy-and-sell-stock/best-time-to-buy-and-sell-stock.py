class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## Length of array
        n = len(prices)

        ## Initialize required variables
        minBuy = prices[0]
        maxProfit = 0

        ## Iterate over the array
        for index in range(n):
            maxProfit = max(maxProfit, prices[index]-minBuy)
            minBuy = min(minBuy, prices[index])

        ## Return maxProfit 
        return maxProfit