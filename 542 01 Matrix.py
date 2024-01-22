class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        # list that shows the order to process
        process_list = []

        # loop through matrix to find all 0s, add them to list to process, find all 1s, replace with -1 to better distinguish
        for index_i, i in enumerate(mat):
            for index_j, j in enumerate(i):
                if j == 0:
                    process_list.append([index_i, index_j])
                else:
                    mat[index_i][index_j] = -1
        
        # List the direction of the seach
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # Process list of 0s first, add nearby 1s to the list to process later
        while process_list:
            cur = process_list.pop(0)
            for _ in direction:
                new = [cur[0] + _[0], cur[1] + _[1]]

                # new position in bound and is not 0
                if -1 < new[0] < len(mat) and -1 < new[1] < len(mat[0]) and mat[new[0]][new[1]] == -1 and new not in process_list:
                    process_list.append(new)
                    mat[new[0]][new[1]] = mat[cur[0]][cur[1]] + 1
        return mat

# Time complexity: O(n)
# Space complecity: O(n)