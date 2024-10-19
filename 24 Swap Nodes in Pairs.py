# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = head
        pre = dummy
        while cur and cur.next:
            next = cur.next
            cur.next = next.next
            pre.next = next
            next.next = cur

            pre = cur
            cur = cur.next
        return dummy.next

# T: O(n) S: O(1)