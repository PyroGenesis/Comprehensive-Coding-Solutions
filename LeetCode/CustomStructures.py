# these are the data structures I defined myself

class DSU:    
    def __init__(self, size):
        self.parent = list(range(size)) # ith value is the parent node to node i
        self.rank = [1] * size          # max depth of subtree rooted here (used for union by rank)
        
    def find(self, x):
        # if the node is not its own parent, we need to recurse on parent
        if x != self.parent[x]:
            # path compression
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    # returns a boolean whether or not union was needed
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)        
        
        if rootX == rootY:
            # no union needed
            return False
        
        if self.rank[rootX] > self.rank[rootY]:
            # rootX has deeper subtree, therefore set it as parent to rootY (and its subtree)
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            # rootY has deeper subtree, therefore set it as parent to rootX (and its subtree)
            self.parent[rootX] = rootY
        else:
            # both subtrees are of equal depth, therefore choose either one of them as the parent of the other
            # here we chose rootX as the parent of rootY, therefore rootX depth increases by 1
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        
        # union complete
        return True
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)