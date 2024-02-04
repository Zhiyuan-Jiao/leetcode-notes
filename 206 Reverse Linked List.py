# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        pre = None
        
        while cur:
            after = cur.next
            cur.next = pre
            pre = cur
            cur = after

        return pre

# Note: create a after variable for each iteration to record the next node, easy to check for while loop too