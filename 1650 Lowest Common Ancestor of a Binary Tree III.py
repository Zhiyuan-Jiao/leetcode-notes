"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
    #     pSet = set()
    #     while p:
    #         pSet.add(p)
    #         p = p.parent
    #     while q:
    #         if q in pSet:
    #             return q
    #         q = q.parent
    # # Time complexity: O(n)
    # # Space complexity: O(h)

        # p1, p2 = p, q
        # while p1 != p2:
        #     p1 = p1.parent if p1.parent else q
        #     p2 = p2.parent if p2.parent else p
        # return p1
        
    # Note: 

        def getDepth(node):
            depth = 0
            while node.parent:
                node = node.parent
                depth += 1
            return depth
        
        dp, dq = getDepth(p), getDepth(q)
        while dp > dq:
            p = p.parent
            dp -= 1
        while dp < dq:
            q = q.parent
            dq -= 1
        while p != q:
            p = p.parent
            q = q.parent
        return p
    
    # Note: get them at the same level first
    # Time complexity: O(h)
    # Space complexity: O(1)