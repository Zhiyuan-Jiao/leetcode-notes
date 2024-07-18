# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        rootVal = postorder[-1]
        rootIdx = inorder.index(rootVal)
        root = TreeNode(rootVal)

        inorderRight = inorder[rootIdx + 1:]
        postorderRight = postorder[-len(inorderRight) - 1: -1]
        if inorderRight and postorderRight:
            root.right = self.buildTree(inorderRight, postorderRight)

        inorderLeft = inorder[:rootIdx]
        postorderLeft = postorder[:len(inorderLeft)]
        if inorderLeft and postorderLeft:
            root.left = self.buildTree(inorderLeft, postorderLeft)
        return root

# T: O(n) S: O(logn)