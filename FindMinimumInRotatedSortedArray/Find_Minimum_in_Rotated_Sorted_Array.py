class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0 , len(nums) - 1
        mini = nums[0]
        
        while l <= r:
            # checking if current part of array is sorted?
            if nums[l] < nums[r]:
                mini = min(mini , nums[l])
                break
                        
            mid = (l + r) // 2   
            mini = min(mini , nums[mid])
            # if left most value is less the mid
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
                
        return mini
