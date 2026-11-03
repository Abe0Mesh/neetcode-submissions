class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        i = 0
        j = i + 1

        while j < len(prices):

            # lowest i and the highest j
            # if i > j, shift both pointers
            # else move j to the right, calculate new profit and see if its better thent he max profit

            if prices[i] > prices[j]:
                i = j
                j += 1
                
                continue
            
            
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit

            j += 1

        
        return max_profit

        