class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Sol 1
        filteredStr = ''
        """
        Step 1:
        Itereat though every char in str
        and remove all non Alphanumeric 
        using python's isalnum() function

        step 2:
        change all char to lower case

        step 3:
        reverse the str 

        step 4:
        return the compair them

        """
        for char in s :
            if char.isalnum() :
                filteredStr += char.lower()
        
        return filteredStr == filteredStr[::-1]

        # Sol 2

        