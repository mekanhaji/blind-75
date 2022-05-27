# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr , prev = head , None
        
        while curr :
            # storing the broken link 
            nxt = curr.next
            # changing link
            curr.next = prev
            # moving the pointers
            prev = curr
            curr = nxt
        return prev