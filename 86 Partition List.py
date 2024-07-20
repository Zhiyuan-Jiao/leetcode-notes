# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        smallerNodes = dummy1 = ListNode(0)
        dummy2 = ListNode(0, head)
        cur = dummy2
        while cur.next:
            while cur.next and cur.next.val < x:
                smallerNodes.next = cur.next
                cur.next = cur.next.next
                smallerNodes = smallerNodes.next
                smallerNodes.next = None
            cur = cur.next if cur.next else cur
        smallerNodes.next = dummy2.next
        return dummy1.next

# T: O(n) S: O(1)