class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        sqr = collections.defaultdict(set) # key = (r /3, c /3)

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val == ".": continue
                if val in row[r] or val in col[c] or val in sqr[(r // 3, c // 3)]:
                    return False
                row[r].add(val)
                col[c].add(val)
                sqr[(r // 3, c // 3)].add(val)
        return True
    
# Time complexity: O(n)
# Space complexity: O(n)