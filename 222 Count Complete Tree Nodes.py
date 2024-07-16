# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getHeight(root):
            h = -1
            while root:
                h += 1
                root = root.left
            return h
        
        fullH = getHeight(root)
        res = 0
        while root:
            print(res)
            if getHeight(root.right) == fullH - 1:
                root = root.right
                res += 2 ** fullH
            else:
                res += 2 ** (fullH - 1)
                root  = root.left
            fullH -= 1
        return res

# Note: Use binary search to check if right subtree is complete, if yes add all nodes at left subtree to res, 
# if not add all nodes at right subtree to res.
# T: O(logn*logn) S: O(1)