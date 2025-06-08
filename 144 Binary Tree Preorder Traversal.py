# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # stack = []
        # res = []
        # cur = root
        # while stack or cur:
        #     if cur.right: stack.append(cur.right)
        #     if cur.left: stack.append(cur.left)
        #     res.append(cur.val)
        #     cur = stack.pop() if stack else None
        # return res

        res = []
        cur = root
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if prev.right:
                    prev.right = None
                    cur = cur.right
                else:
                    prev.right = cur
                    res.append(cur.val)
                    cur = cur.left
        return res
                