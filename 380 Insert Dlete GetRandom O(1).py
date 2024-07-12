class RandomizedSet:

    def __init__(self):
        self.l = []
        self.hashMap = {}
        

    def insert(self, val: int) -> bool:
        if val in self.hashMap:
            return False
        else:
            self.l.append(val)
            self.hashMap[val] = len(self.l) - 1
            return True
        

    def remove(self, val: int) -> bool:
        if val not in self.hashMap:
            return False
        else:
            idx = self.hashMap[val]
            self.l[idx] = self.l[-1]
            self.hashMap[self.l[-1]] = idx
            self.l.pop()
            self.hashMap.pop(val)
            return True
        

    def getRandom(self) -> int:
        return random.choice(self.l)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# Note: Use a list track all the elements for random choose, use a hashmap with val key point to list index
# when remove an element, swap the last element with the element needed to remove and pop from the last to achieve O(1)