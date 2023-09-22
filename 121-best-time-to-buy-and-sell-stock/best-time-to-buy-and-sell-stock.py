class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(0,len(prices)-1):
            buy_val = prices[i]

            if i == 0:
                sell_val = max(prices[i+1:])
            if prices[i] == sell_val and buy_val != 0:
                sell_val = max(prices[i+1:])

            if max_profit < sell_val-buy_val:
                max_profit = sell_val-buy_val

        return max_profit
        