"""
Given a directed graph, return an array of nodes where 
each node appears before all the nodes it points to.

Time complexity: O(|V| + |E|)
    - |V| is the number of vertices
    - |E| is the number of edges
    
Space complexity: O(|V|)
"""

### Kahn's Algorithm ###
from collections import deque
class SolutionKahn:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create adj list and track degree of each node (number of incoming edges)
        degree = [0]*numCourses
        adj = [set() for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[prereq].add(course)
            degree[course] += 1
        
        # implement topological sort using Kahn's algorithm
        queue = deque([i for i in range(numCourses) if degree[i] == 0])
        topsort = []
            
        while queue:
            course = queue.popleft()
            topsort.append(course)
            # iterate through neighboring nodes and reduce degree by 1
            for course_next in adj[course]:
                degree[course_next] -= 1
                # nodes in a cycle would never have degree 0,
                # so they would never be added to the queue
                if degree[course_next] == 0:
                    queue.append(course_next)
        
        # if there is a cycle, not all nodes will have degree 0, 
        # which means not all nodes have been added to the list "topsort"
        if len(topsort) != numCourses:
            return []
        return topsort
        

### DFS solution ###
class SolutionDfs:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create adj list
        adj = [set() for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[prereq].add(course)
            
        ### dfs method
        # visited[i] == 0 means not visited, 1 means has visited, -1 means is visiting
        visited = [0 for course in range(numCourses)]
        self.ans = []
        self.is_possible = True # true if topological order is possible
        for i in range(numCourses):
            self.dfs(i, visited, adj)
            if not self.is_possible: 
                return []
        return self.ans[::-1]
        
    def dfs(self, node, visited, adj):
        # going to a node that you are "visiting" means you have a cycle
        # and a topological ordering is impossible
        if visited[node] == -1:
            self.is_possible = False
            return
        if visited[node] == 1:
            return
        
        visited[node] = -1
        for neighbor in adj[node]:
            self.dfs(neighbor, visited, adj)
        self.ans.append(node) # append in reverse topological order
        visited[node] = 1
        
