class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()
        start = 0
        length = 0
        
        for end in range(len(s)):
            while s[end] in myset:
                myset.remove(s[start])
                start += 1
            myset.add(s[end])
            length = max(length , end - (start - 1))
            
        return length
