# Time O(32)
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            """
            Check The last Bit...
            Method 1: (Do & operation to n with 1)
                n & 1
            ex 1:  1001     1010
                 & 0001   & 0001
                  ------  -------
                   0001     0000
                  ------  ------- 
            Method 2: (Same can be axhive by doing
            n mod 2 )
                n % 2
            """
            
            # Stor
            res += n & 1
            
            # Swift bits by one to chack next bit
            n = n >> 1
        return res
      
# Time O(no. of 1's Bit)      
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res
