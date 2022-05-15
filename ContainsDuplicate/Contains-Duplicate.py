class Solution:
    def containsDuplicate(self, arr: List[int]) -> bool:
        n = len(arr) #length of arr
        """
        1. brutforce approch :
          time -> O(n^2)
          space -> O(1)
        """
        for i in range(0,n): # <- n times
          for j in range(i + 1,n):# <- n times
            if arr[i] == arr[j]:
              return True
        return False
        
        """
        2. Sorting approch :
          time -> O(n*log(n))
          space -> O(1)
          Runtime -> 605 ms
          Memory Usage -> 22.3 MB
        """
        arr.sort() # <- n*log(n) times
        for i in range(0,n - 1): # <- n times
          if arr[i] == arr[i + 1]:
            return True
        return False
        
        """
        3. Using HashSet :
          time -> O(n)
          space -> O(n)
          Runtime -> 724 ms
          Memory Usage -> 24  MB
        """
        arrset = set() # <- space O(n)
        for i in range(0,n): # <- time O(n)
          if arr[i] in arrset:
            return True
          arrset.add(arr[i])
        return False
        """
        4. Using HashSet :
          time -> O(1)
          space -> O(n)
          Runtime -> 416 ms
          Memory Usage -> 24.1 MB
        """
        return True if len(set(arr)) < len(arr) else False