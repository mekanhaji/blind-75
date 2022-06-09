class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # key -> element , values -> frequecy
        
        # buket to store frequency
        #  1                            2           ...n
        # [ele..s with freq 1 ] [ele. with freq 2 ] ... 
        freq = [ [] for i in range(len(nums) + 1)]
        
        
        # count the frequency
        for n in nums :
            count[n] = 1 + count.get(n , 0)
        # Putting in buket
        for n , c in count.items():
            freq[c].append(n)
        
        
        # result
        res = []
        # itreating backwords
        for i in range(len(freq) - 1, 0, -1):
             
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
