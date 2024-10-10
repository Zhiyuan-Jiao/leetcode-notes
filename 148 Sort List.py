# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head or not head.next:
            return head
        
        mid = self.getMid(head)
        l1 = head
        l2 = mid.next
        mid.next = None

        l1 = self.sortList(l1)
        l2 = self.sortList(l2)
        return self.merge(l1, l2)

    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, l1, l2):
        cur = dummy = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
        return dummy.next

# Time complexity: O(nlogn) Space complexity: O(logn)
# Note: merge sort