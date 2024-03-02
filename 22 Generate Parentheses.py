class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
# DFS:
# 				(0, 0, '')
# 			 	    |	
# 				(1, 0, '(')  
# 			   /           \
# 		(2, 0, '((')      (1, 1, '()')
# 		   /                 \
# 	(2, 1, '(()')           (2, 1, '()(')
# 	   /                       \
# (2, 2, '(())')                (2, 2, '()()')
# 	      |	                             |
# res.append('(())')             res.append('()()')
        def dfs(left, right, s):
            # base case
            if len(s) == n * 2:
                res.append(s)
                return
            
            # add left
            if left < n:
                dfs(left + 1, right, s + "(")
            # add right
            if right < left:
                dfs(left, right + 1, s + ")")
        
        res = []
        dfs(0, 0, "")
        return res

# Time complexity: O(n)
# Space complexity: O(1)