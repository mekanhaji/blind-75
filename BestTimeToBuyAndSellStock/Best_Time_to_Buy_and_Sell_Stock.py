class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0 , 1
        maxprofit = 0
        
        while r < len(prices) :
            # profitable ?
            if prices[r] > prices[l] :
                profit = prices[r] - prices[l]
                maxProfit = max(profit , maxProfit)
            else :
                # if it isn't profitable 
                # update left (l) where right (r) 
                # resion : at this point r will be lower then l 
                # and every value beform r. so, we can just update l to r...
                # [7,2,5,1,3,0]       [7,2,5,1,3,0]
                #    ^   ^       ==>         ^ ^
                #    l   r                ...l r
                l = r 
            r += 1
            
        return maxProfit