class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        
        for i in nums :
            currSum += i
            
            # after adding each elemenr , check..
            # if currSum is more then maxSum...
            maxSum = max(currSum , maxSum)
            
            # if currSum become less then zero..
            # we will remove prev. sum of element's
            #and reset currSum to 0 and start again from that point
            if currSum < 0 : currSum = 0
            
        
        return maxSum
