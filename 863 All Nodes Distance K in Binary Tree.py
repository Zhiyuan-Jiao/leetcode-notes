# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        def dfs(root):
            if not root:
                return 
            if root.left:
                parent[root.left] = root
                dfs(root.left)
            if root.right:
                parent[root.right] = root
                dfs(root.right)
        dfs(root)

        res = []
        q = deque([target])
        depth = 0
        visited = set()
        while depth <= k and q:
            for i in range(len(q)):
                node = q.popleft()
                if node in visited: continue
                visited.add(node)
                if depth == k: res.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                if node in parent: q.append(parent[node])
            depth += 1
        return res
