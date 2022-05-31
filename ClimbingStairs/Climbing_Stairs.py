class Solution:
    def climbStairs(self, n: int) -> int:
        # Base Canditon...
        if n <= 3 : return n
        
        one , two = 2 , 3
        
        """
        steps : 4 | 5 | 6  | 7  | 8  | 9  |...|    n     |
        --------------------------------------------------
        one   : 3 | 5 | 8  | 13 | 21 | 34 |...|    two   |
        --------------------------------------------------
        two   : 5 | 8 | 13 | 21 | 34 | 55 |...| one + two| <- Result | No Of Moves
        --------------------------------------------------
        """
        
        for i in range(4 , n + 1) :
            one , two = two , one + two
            
        return two
