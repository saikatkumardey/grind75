class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit_so_far = 0
        min_price_so_far = prices[0]
        for price_idx in range(1,len(prices)):
            price = prices[price_idx]
            max_profit_so_far = max(max_profit_so_far, price - min_price_so_far)
            min_price_so_far = min(min_price_so_far, price)
        return max_profit_so_far