# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(cur, node):
            nonlocal res

            cur += str(node.val)
            # end node of tree
            if not node.left and not node.right:
                res += int(cur)
                return
            
            if node.left:
                dfs(cur, node.left)
            if node.right:
                dfs(cur, node.right)

        dfs("", root)
        return res

    # T: O(n) S: O(H)

# morris traversal
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        cur = root
        res = 0
        while cur:
            if cur.left:
                # find predecessor
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                # thread already exist
                if pre.right:
                    pre.right = None
                    if not pre.left:
                        res += pre.val
                    cur.val -= 10 * pre.val
                    if cur.right:
                        cur.right.val += 10 * cur.val
                    cur = cur.right
                    continue
                # create thread
                pre.right = cur
                cur.left.val += 10 * cur.val
                cur = cur.left
            else:
                if cur.right:
                    cur.right.val += 10 * cur.val
                else:
                    res += cur.val
                cur = cur.right
        return res
    
    # T: O(n) S: O(1)