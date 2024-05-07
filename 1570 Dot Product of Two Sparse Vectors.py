class SparseVector:
    # def __init__(self, nums: List[int]):
    #     self.hashMap = {}
    #     for i, n in enumerate(nums):
    #         self.hashMap[i] = n

    # # Return the dotProduct of two sparse vectors
    # def dotProduct(self, vec: 'SparseVector') -> int:
    #     res = 0
    #     for i in self.hashMap:
    #         if i in vec.hashMap:
    #             res += vec.hashMap[i] * self.hashMap[i]
    #     return res

    # Note: the downside of it is that hashmap/dict's hashcode is a reference to a linkedlist object(or array depending on the implementation).
    #       So, it could refer to a place very far away in memeory(even likely refer to the disk location).

    def __init__(self, nums: List[int]):
        self.idx_val = [[i, n] for i, n in enumerate(nums) if n != 0]

    def dotProduct(self, vec: 'SparseVector') -> int:
        p1, p2, res = 0, 0, 0
        while p1 < len(self.idx_val) and p2 < len(vec.idx_val):
            if self.idx_val[p1][0] == vec.idx_val[p2][0]:
                res += self.idx_val[p1][1] * vec.idx_val[p2][1]
                p1 += 1
                p2 += 1
            elif self.idx_val[p1][0] > vec.idx_val[p2][0]:
                p2 += 1
            else:
                p1 += 1
        return res

# Note: Create two list and use two pointer to get the product

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

# Follow up:
# What if only one vector is sparse and the other is full of non-zero values?
# We still use idx_val pair to form the new vector. But this time, instead of using two pointer method, we can simply do binary search on the idx_val pair list formulated by the sparse vector.
# eg:
# tuple is in the format (idx, val).
# res = 0
# sparse_vec = [(5, 2), (7, 8)]
# full_vec = [(1, 2), (2, 4), (3, 5), (4, 6), (7, 19)]
# We do binary search to find the idx position 5, since there isn't a tuple with idx = 5 we return 'inf' indicating none valid idx found.
# We do binary search to find the idx position 7. And we successfully find the tuple with idx = 7 in full_vec has the val = 19. We do res += 8 * 19.