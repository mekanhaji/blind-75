class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sol 1
        """
        Sorting
            By sorting the String they will be same (equel)
            Ex. -> 'zatazt' and 'azaztt' will become 'aattzz'
        """
        return sorted(s) == sorted(t)
        # Sol 2
        """
        Cheacking For length
            For being anagram they shoud be of same length
        """
        if len(s) != len(t):
            return False
        """
        Creating HashMap
            we'll map every char with it's number of time occurred
            key   -> char
            value -> occurence
        """
        s_hash , t_hash = {} , {}
        
        for i in range(len(s)):
            #  Key                  Value
            s_hash[s[i]] = 1 + s_hash.get(s[i] , 0)
            t_hash[t[i]] = 1 + t_hash.get(t[i] , 0)
            
        for c in s_hash :
            if s_hash[c] != t_hash.get(c , 0):
                return False
        return True

        # Sol 3
        """
        Using Counter()
            Counter is a subclass of dict that's specially designed for counting hashable objects in Python
        """
        return Counter(s) == Counter(t)