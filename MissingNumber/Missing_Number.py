class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # cheching for each number inrange [0 , n],
        # if it's not present return that number...
        for i in range(0 , len(nums) + 1):
            if i not in nums:
                return i

# Sorting ... time -> O(2n.logn)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return nums[-1] + 1
# 
