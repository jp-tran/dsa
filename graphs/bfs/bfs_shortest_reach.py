# find distance to any node in an undirected graph using bfs

import math
import os
import random
import re
import sys

# Complete the bfs function below.
def bfs(n, m, edges, s):
    #create an adjacency list
    adj_list = [set() for _ in range(n)] #zero-indexed
    for edge in edges:
        adj_list[edge[0]-1].add(edge[1])
        adj_list[edge[1]-1].add(edge[0])

    explored = [False]*n #zero-indexed
    explored[s-1] = True
    dist = [-1]*n #zero-indexed
    dist[s-1] = 0 #distance at starting node is zero
    queue = [s] #queue to track order of nodes to explore
    while queue:
        v = queue.pop(0) #current vertex
        for w in adj_list[v-1]:
            if not explored[w-1]:
                explored[w-1] = True
                queue.append(w)
                dist[w-1] = dist[v-1] + 6
    # print(adj_list)
    # print(explored)
    return dist[:s-1] + dist[s:]

            
if __name__ == '__main__':
    with open('input.txt') as input_f:

        q = int(input_f.readline())

        for q_itr in range(q):
            nm = input_f.readline().split()

            n = int(nm[0])

            m = int(nm[1])

            edges = []

            for _ in range(m):
                edges.append(list(map(int, input_f.readline().rstrip().split())))

            s = int(input_f.readline())

            result = bfs(n, m, edges, s)

            print(' '.join(map(str, result)))

        # fptr.close()
