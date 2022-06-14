# Time O(26 * n)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # key -> char , val -> freq
        ans = 0
        
        start = 0
        for end in range(len(s)):
            count[s[end]] = 1 + count.get(s[end] , 0)
            
            # untile window in not valid move start pointer
            while (end - start + 1) - max(count.values()) > k:
                # decrese count of starting char
                count[s[start]] -= 1
                start += 1
            ans = max(ans , (end - start + 1))
            
        return ans
      
# Time O(n)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # key -> char , val -> freq
        ans = 0
        maxf = 0 # max freq of char
        
        start = 0
        for end in range(len(s)):
            count[s[end]] = 1 + count.get(s[end] , 0)
            # Updating maxf 
            maxf = max(maxf , count[s[end]])
            
            # untile window in not valid move start pointer
            while (end - start + 1) - maxf > k:
                # decrese count of starting char
                count[s[start]] -= 1
                start += 1
            
            ans = max(ans , (end - start + 1))
            
        return ans
