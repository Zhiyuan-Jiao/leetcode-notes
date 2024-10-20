# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        one, two = headA, headB
        while one != two:
            one = headB if one is None else one.next
            two = headA if two is None else two.next
        return one

# T: O(n) S: O(1)
# Note: Use two pointer to each iterate both linked list
# The difference in length in the first iteration will offset and match them in the second iteration