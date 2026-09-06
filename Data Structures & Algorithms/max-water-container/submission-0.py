class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxs = 0
        # pointer problem
        left ,right = 0,len(heights)-1
        while(left<right):
            minpr = min(heights[left],heights[right])
            prod = minpr* (right-left)
            maxs = max(prod,maxs)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maxs