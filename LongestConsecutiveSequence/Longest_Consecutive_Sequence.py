class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        
        # for empty array...
        longest = 0
        
        # Itreating [nums]
        for i in nums:
            # Check for,
            # if it's starting of are sequence or not !?
            if (i - 1) not in numSet:
                # cound the length of sequence...
                length = 1
                
                # i + length eg. 6 -> 6 + 1 -> 6 + 2 ...
                while (i + length) in numSet :
                    length += 1
                
                # Updating Longest count
                longest = max(length , longest)
                
        return longest
