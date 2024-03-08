# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
# Use list brute force

        # l = []
        # cur = head
        # while cur:
        #     l.append(cur)
        #     cur = cur.next

        # cur = dummy = ListNode()
        # left, right = 0, len(l) - 1
        # while left < right:
        #     cur.next = l[left]
        #     cur = cur.next
        #     cur.next = l[right]
        #     cur = cur.next
        #     left += 1
        #     right -= 1
        # if left == right: # add mid when len is odd
        #     cur.next = l[left]
        #     cur = cur.next
        # cur.next = None
        
        # return dummy.next

# Time complexity: O(n)
# Space complexity: O(n)

# Use slow fast pointer

        if not head.next: return

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        pre = slow.next
        cur = pre.next
        slow.next = pre.next = None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        s1, s2 = head, pre

        while s2:
            s1Next = s1.next
            s1.next = s2
            s1 = s1Next
            s2Next = s2.next
            s2.next = s1
            s2 = s2Next
        
# Time complexity: O(n)
# Space complexity: O(1)
