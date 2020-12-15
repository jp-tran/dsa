from collections import defaultdict

### for m operations and n nodes, time complexity is O(m alpha(n))
### for practical purposes, O(alpha(n)) is constant, so final complexity is O(m)

class Node:
    def __init__(self, value, parent = None, rank = 0):
        self.val = value
        self.parent = parent
        self.rank = rank

class DisjointSet:
    def __init__(self):
        self.hashtable = {}
    
    def makeSet(self, val):
        """Create a set with only one element."""
        node = Node(val)
        node.parent = node
        self.hashtable[val] = node
        
    def find(self, node):
        """Find uppermost ancestor of node using path compression."""
        if node.parent == node:
            return node
        node.parent = self.find(node.parent)
        return node.parent
        
    def union(self, val1, val2):
        """Union of two sets by rank.
        Returns true if val1 and val2 are in different sets before the union
        """
        if val1 not in self.hashtable:
            self.makeSet(val1)
        if val2 not in self.hashtable:
            self.makeSet(val2)
        node1 = self.hashtable[val1]
        node2 = self.hashtable[val2]
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        
        # if they are part of the same set
        if parent1.val == parent2.val:
            return False
        # else the node with the higher rank becomes the parent of the other node
        elif parent1.rank < parent2.rank:
            parent1.parent = parent2
        elif parent1.rank > parent2.rank:
            parent2.parent = parent1
        else:
            parent1.parent = parent2
            parent2.rank += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ds = DisjointSet()
        for u, v in edges:
            are_in_same_set = not ds.union(u, v)
            # if nodes of an edge are in the same set before union, 
            # the edge is redundant
            if are_in_same_set:
                return [u, v]
                