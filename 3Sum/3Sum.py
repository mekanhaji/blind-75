class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i , a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l , r = i + 1 , len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a , nums[l] , nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res
#---------------------------------------------------------------------------------------------------------------------#
# Sol using Set
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        solutions = set()  # as to only keep unique solutions, we maintain a set of solutions
        nums.sort()  # NOTE that we sort the numbers
        
        # we iterate over (almost) all the numbers and consider the current number fixed
        # the problem is then to find a 2-combination of numbers on the right of the fixed number
        # such that they sum up to the additive complement of the fixed number
        for i in range(n - 2):
            j = i + 1  # initial: smallest number not smaller than the fixed number
            k = n - 1  # initial: biggest number overall
            
            while j < k:
                # if (i, j, k) is a solution, store it in the solution set
                triplet_sum = nums[i] + nums[j] + nums[k]
                if triplet_sum == 0:
                    solutions.add((nums[i], nums[j], nums[k]))
                    
                # if the sum is negative, nums[j] must be bigger -> move to right
                # we also move j to the right if we found a solution to guarantee termination of the while loop
                if triplet_sum <= 0:  
                    j += 1
                elif triplet_sum > 0:  # if the sum is negative, nums[k] must be smaller -> move to left
                    k -= 1
                    
        # return solutions as a list of lists by mapping each tuple in the set to a list
        return list(map(list, solutions))
