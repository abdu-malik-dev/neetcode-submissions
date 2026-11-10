class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        maxprofit = 0 

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                diff = prices[right] - prices[left]
                maxprofit = max(diff, maxprofit)

            right += 1
                
        return maxprofit

