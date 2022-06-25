# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = ListNode(0 , head)
        f , s = tmp , head
        
        while n > 0 and s:
            s = s.next
            n -= 1
        
        while s:
            f = f.next
            s = s.next
        
        # delete
        f.next = f.next.next
                
        return tmp.next
