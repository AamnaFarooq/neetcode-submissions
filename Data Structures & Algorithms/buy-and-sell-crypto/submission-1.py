class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #you want to buy the minimum price first
        # and sell it with the biggese proces

        max_profit = 0
        min_price = prices[0]
        min_index = 0

        #is this the chepaest price ive seen so far
        #if i sold this, is it the best profit, ive seen so far
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
                min_index = i
                 
            if prices[i] - min_price >= 0:
                max_profit =  max(prices[i] - min_price, max_profit)

                print(f"max profit: {max_profit}" )

        return max_profit 




        