class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        maxProfit = 0
        while r < len(prices) - 1 or l < len(prices) - 1:
            profit = prices[r] - prices[l]
            print(profit, r, l)
            if profit < 0:
                l += 1
            
            if profit >= 0:
                maxProfit = max(maxProfit, profit)
                if r < len(prices) - 1:
                    r += 1
                else:
                    print("hello!", r, l)
                    l += 1
            
            
            if l == r:
                r += 1
        
        return maxProfit