class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderDFS(root):
    stack, res = [root], []
    while stack:
        cur = stack.pop()
        res.append(cur.val)
        if cur.right: stack.append(cur.right)
        if cur.left: stack.append(cur.left)
    return res

def inorderDFS(root):
    stack, cur, res = [], root, []
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res

def postorderDFS(root):
    stack, res = [root], []
    while stack:
        cur = stack.pop()
        res.append(cur.val)
        if cur.left: stack.append(cur.left)
        if cur.right: stack.append(cur.right)
    return res[::-1]
    

# Example tree:
#     1
#    / \
#   2   3
#  / \
# 4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Preorder Traversal:", preorderDFS(root))
print("Inorder Traversal:", inorderDFS(root))
print("Postorder Traversal:", postorderDFS(root))