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
# Math... time -> O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for i in nums:
            sum += i
        n = len(nums)
        sumn = (n * (n + 1)) / 2
        return int(sumn - sum)
#
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        
        for i in range(len(nums)):
            res += (i - nums[i])
        return res
