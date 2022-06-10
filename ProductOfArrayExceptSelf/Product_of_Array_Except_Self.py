class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Result Array..
        # At initial [1 , 1 ,1 , ...] with size of input array
        res = [1] * len(nums)
        
        # Prefix Product...
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        # Postfix Product...
        prosfix = 1
        for i in range(len(nums) - 1 , -1 , -1):
            # Postfix[i + 1] * Prefix[i - 1]
            res[i] *= prosfix
            prosfix *= nums[i]
            
        return res
