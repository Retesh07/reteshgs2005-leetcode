class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        sell=1
        profit=0
        while sell<len(prices):
            if prices[buy]>prices[sell]:
                buy=sell
            
            temp=prices[sell]-prices[buy]
            profit=max(temp,profit)
            sell+=1
            
        return profit


            



        