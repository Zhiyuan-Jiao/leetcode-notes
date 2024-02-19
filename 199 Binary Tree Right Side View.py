# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return res

        q = collections.deque([root])
        while q:
            rightside = None

            for i in range(len(q)):
                node = q.popleft()

                rightside = node
                if node.left: q.append(node.left) 
                if node.right: q.append(node.right)
            
            res.append(rightside.val)
        
        return res

# Algorithm: BFS (Reverse Order traversal): get the last node in each level
# Time complexity: O(n)
# Space complexity: O(n)