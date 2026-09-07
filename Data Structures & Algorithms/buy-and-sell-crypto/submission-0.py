class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxprofit= 0
        while right<len(prices):
            if prices[left]<prices[right]:
                maxprofit = max(prices[right]-prices[left], maxprofit)
            else:
                left = right
            right+=1
        return maxprofit
        