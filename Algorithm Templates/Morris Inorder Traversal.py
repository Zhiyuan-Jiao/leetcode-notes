class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def morris_inorder_traversal(root):
    cur = root
    while cur:
        if cur.left:
            # Find predecessor
            pre = cur.left
            while pre.right and pre.right != cur:
                pre = pre.right
            # Thread already existed
            if pre.right:
                pre.right = None
                print(cur.val)
                cur = cur.right
                continue
            # Create thread
            pre.right = cur
            cur = cur.left
        else:
            print(cur.val)
            cur = cur.right

# Create the tree
#       4
#      / \
#     2   5
#    / \
#   1   3

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

# Perform Morris Inorder Traversal
print("Inorder Traversal using Morris Method:")
morris_inorder_traversal(root)
