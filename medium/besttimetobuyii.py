class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        entry = 0
        bought = False

        for i in range(len(prices)):
            if i == len(prices) - 1:
                if bought == True: #sell signal
                    bought = False
                    profit += (prices[i] - entry)
            
            else:
                if prices[i+1] > prices[i] and bought == False: #buy signal
                    bought = True
                    entry = prices[i]
                
                if (prices[i+1] < prices[i] or i == len(prices)) and bought == True: #sell signal
                    bought = False
                    profit += (prices[i] - entry)
        
        
        return profit