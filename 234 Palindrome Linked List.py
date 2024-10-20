# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        # stack = []
        # cur = head
        # while cur:
        #     stack.append(cur.val)
        #     cur = cur.next
        # cur = head
        # while cur:
        #     if cur.val != stack.pop():
        #         return False
        #     cur = cur.next
        # return True

# T: O(n) S: O(n)

        def reverse(head):
            pre = dummy = ListNode(0)
            cur = head
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            head.next = None
            return pre
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        reversed = reverse(slow.next)
        while reversed:
            if reversed.val != head.val:
                return False
            reversed = reversed.next
            head = head.next
        return True

# T: O(n) S: O(1)
# Note: Use slow fast pointer find mid point then reverse the second half list.
