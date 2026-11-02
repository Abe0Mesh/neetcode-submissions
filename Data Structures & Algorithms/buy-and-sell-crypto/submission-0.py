class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        #index's
        i = 0 # buy index
        j = i + 1 # sell index

        for i in range(len(prices) - 1):
            j = i + 1
            while j < len(prices):
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]
                j+= 1





        # Input: prices = [10,1,5,6,7,1]
        # for 10, 













        return profit