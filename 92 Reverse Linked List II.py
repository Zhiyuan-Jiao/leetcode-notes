# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        def reverse(node, end):
            prev = node
            if prev.next:
                cur = prev.next
                prev.next = end
            else:
                return prev
            while cur:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            return prev
        
        dummy = ListNode(0, head)
        pos = 0
        cur = dummy
        toReverse = None
        beforeL, afterR = None, None
        while cur:
            if pos == left - 1:
                beforeL = cur
                toReverse = cur.next
                cur.next = None
                cur = toReverse
            elif pos == right:
                print(afterR)
                afterR = cur.next
                cur.next = None
                cur = afterR
            else:
                cur = cur.next
            pos += 1
        reversed = reverse(toReverse, afterR)
        beforeL.next = reversed
        return dummy.next

# T: O(n) S: O(1)