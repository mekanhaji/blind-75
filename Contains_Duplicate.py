class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        st = set(nums)
        return len(nums) - len(st)
