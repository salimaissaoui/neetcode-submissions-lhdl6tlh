class Solution:
    from typing import List

    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables
        min_price = float('inf')  # Minimum price seen so far
        max_profit = 0           # Maximum profit

        for price in prices:
            # Update the minimum price
            min_price = min(min_price, price)
            # Calculate the current profit and update max profit if necessary
            max_profit = max(max_profit, price - min_price)

        return max_profit

        