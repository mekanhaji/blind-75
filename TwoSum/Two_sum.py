class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        BrutForce
            Using 2 For Loop(inner and outer)
            1st loop for first value and 2nd for value which
            sums up to the target.
            Time -> O(n^2)
            Space -> O(1) 
        """
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        """
        Using HashMap
            We can map values with index,
            Key   -> Number
            Value -> Index
            Now We will Iterate though are and checking
            if other value(diff = target - num[i]) is in our map.
            Time -> O(n)
            Space -> O(n)
        """
        hashmap = {}
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff] , i]
            hashmap[n] = i
