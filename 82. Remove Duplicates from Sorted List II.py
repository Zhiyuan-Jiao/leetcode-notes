# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next: return head
#         disSet = set()
#         dupSet = set()
#         cur = head
#         while cur:
#             if cur.val in disSet:
#                 dupSet.add(cur.val)
#             else:
#                 disSet.add(cur.val)
#             cur = cur.next
#         prev = dummy = ListNode(0, None)
#         dummy.next = cur = head
#         while cur:
#             while cur and cur.val in dupSet:
#                 cur = cur.next
#             prev.next = cur
#             prev = cur
#             cur = cur.next if cur else None
#         return dummy.next

# # T: O(n) S: O(n)

            dummy = ListNode(float("-inf"), head)
            curr, prev = head, dummy
            while curr:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                
                if prev.next == curr:
                    prev = prev.next
                    curr = curr.next
                else:
                    prev.next = curr.next
                    curr = prev.next
            return dummy.next

# T: O(n) S: O(1)