class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, n):
        # Find root
        root = n
        while self.parent[root] != root:
            root = self.parent[root]
        
        # Path compression
        while self.parent[n] != root:
            parent = self.parent[n]
            self.parent[n] = root
            n = parent

        return root
    
    def union(self, n, m):
        rn, rm = self.find(n), self.find(m)

        if self.rank[rn] >= self.rank[rm]:
            self.parent[rm] = rn
            self.rank[rn] += self.rank[rm]
        else:
            self.parent[rn] = rm
            self.rank[rm] += self.rank[rn]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        # map email to account, merge account when there are duplicate emails
        emailToAccount = {}
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAccount:
                    uf.union(emailToAccount[e], i)
                else:
                    emailToAccount[e] = i
        
        # create email group for each account
        emailGroup = {}
        for e, i in emailToAccount.items():
            leader = uf.find(i)
            if leader not in emailGroup:
                emailGroup[leader] = []
            emailGroup[leader].append(e)
        
        # map to the result format
        res = []
        for i, e in emailGroup.items():
            account = [accounts[i][0]]
            emails = sorted([i for i in e])
            account.extend(emails)
            res.append(account)
        return res
