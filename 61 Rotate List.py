# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        if k == 0 or not head.next:
            return head

        # traverse to get length
        cur, length = head, 0
        while cur:
            length += 1
            cur = cur.next

        # traverse to setup two pointer
        k = k % length
        p1 = dummy = ListNode(0, head)
        p2 = p1
        while k > 0:
            p2 = p2.next
            k -= 1
        while p2.next:
            p1 = p1.next
            p2 = p2.next

        # rotate
        p2.next = head
        dummy.next = p1.next
        p1.next = None
        return dummy.next

# T: O(n), S: O(1)