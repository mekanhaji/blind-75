class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        for c in s :
            if c not in map :
                stack.append(c)
                continue
            # it a closing bracket
            # stack in empty
            # last input brackets are not same
            # we'll return False 
            if not stack or stack[-1] != map[c] :
                return False
            # if not any above case pop the last item
            stack.pop()
            
        return not stack
