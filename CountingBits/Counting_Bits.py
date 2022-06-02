# Sol in time -> O(n.log(n))
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        count = 0
        
        for i in range(0 , n + 1) :
            while i :
                count += i % 2
                i = i >> 1
            ans.append(count)
            count = 0
        return ans

    
# Sol in time -> O(n)
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        
        for i in range(1 , n + 1) :
            if offset * 2 == i :
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp
