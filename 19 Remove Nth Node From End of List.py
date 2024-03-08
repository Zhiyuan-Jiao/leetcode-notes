# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if not head.next: return None

        # cur = head
        # total = 0
        # while cur:
        #     total += 1
        #     cur = cur.next
        # position = total - n

        # cur = dummy = ListNode(0, head)
        # curP = -1
        # while cur:
        #     curP += 1
        #     if curP == position:
        #         cur.next = cur.next.next
        #     cur = cur.next
        # return dummy.next

        # Single traverse using two pointer
        dummy = ListNode(0, head)
        l, r = dummy, head

        while n > 0:
            r = r.next
            n -= 1
        
        while r:
            l, r = l.next, r.next
        
        # delete
        l.next = l.next.next
        
        return dummy.next

# Time complexity: O(n)
# Space complexity: O(1)
