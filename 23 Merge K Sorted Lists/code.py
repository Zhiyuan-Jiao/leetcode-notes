# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None

        def mergeList(a, b):
            head = ListNode()
            cur = head

            while a and b:
                if a.val <= b.val:
                    cur.next = ListNode(a.val)
                    a = a.next
                else:
                    cur.next = ListNode(b.val)
                    b = b.next
                cur = cur.next

            if a: cur.next = a
            if b: cur.next = b

            return head.next
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1, l2 = lists[i], lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(mergeList(l1, l2))
            lists = mergedLists
        
        return lists[0]

# Time complexity: O(nlogk)
# Space complexity: O(n)
