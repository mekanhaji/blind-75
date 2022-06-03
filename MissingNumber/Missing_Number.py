class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # cheching for each number inrange [0 , n],
        # if it's not present return that number...
        for i in range(0 , len(nums) + 1):
            if i not in nums:
                return i
