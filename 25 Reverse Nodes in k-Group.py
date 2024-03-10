# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head

        def reverse(node):
            pre = None
            cur = node
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre, node

        p1 = p2 = head
        n = k
        while n > 1:
            if not p2 or not p2.next: return head
            p2 = p2.next
            n -= 1
        
        pre = dummy = ListNode()
        while True:
            remain = p2.next
            p2.next = None
            pHead, pEnd = reverse(p1)
            pre.next = pHead
            pEnd.next = remain

            pre = pEnd
            p1 = p2 = remain
            n = k
            while n > 1:
                if not p2 or not p2.next: return dummy.next
                p2 = p2.next
                n -= 1
            
# Time complexity: O(n)
# Space complexity: O(1)