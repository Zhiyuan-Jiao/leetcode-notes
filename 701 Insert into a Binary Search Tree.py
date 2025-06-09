# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if not root: return TreeNode(val)
        # if val < root.val:
        #     root.left = self.insertIntoBST(root.left, val) if root.left else TreeNode(val)
        # else:
        #     root.right = self.insertIntoBST(root.right, val) if root.right else TreeNode(val)
        # return root
        if not root: return TreeNode(val)
        cur = root
        while cur:
            if val < cur.val:
                if cur.left: cur = cur.left
                else: 
                    cur.left = TreeNode(val)
                    break
            else:
                if cur.right: cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    break
        return root
        