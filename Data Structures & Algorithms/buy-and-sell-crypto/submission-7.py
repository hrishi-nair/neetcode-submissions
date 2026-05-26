class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_val = 0
        for i in range(len(prices)):
            if prices[i] < prices[min_val]:
                min_val = i
            elif prices[i] - prices[min_val] > profit:
                profit = prices[i] - prices[min_val]
        return profit
