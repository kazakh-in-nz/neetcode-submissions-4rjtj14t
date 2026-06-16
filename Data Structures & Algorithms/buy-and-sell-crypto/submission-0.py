class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        buy = 0
        profit = 0

        for sell in range(1, len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
                continue
            profit = max(profit, prices[sell] - prices[buy])

        return profit
        