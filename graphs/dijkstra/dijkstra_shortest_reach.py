# implementation of dijkstra's algorithm

import math
import os
import random
import re
import sys
import heapq


def shortestReach(n: int, edges: list, s: int) -> list:
    '''
    n: number of nodes
    edges: list of lists [[beginning node, ending node, edge length], ...]
    s: starting node
    returns a list of shortest distance from s to each node, excluding s
    '''
    #create adjacency list for undirected graph
    adj_list = {i: set() for i in range(1, n+1)}
    for begin, end, length in edges:
        adj_list[begin].add((end, length))
        adj_list[end].add((begin, length))

    queue = [(0, s)] #list of tuples that will be used as a min-heap for Dijkstra's greedy score
    dist = {i: float('inf') for i in range(1, n+1)} #dict of shortest distance to each node
    dist[s] = 0
    explored = {i: False for i in range(1, n+1)} #dict of explored state for each node

    #loop through priority queue until it's empty
    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        if explored[cur_node]: continue
        explored[cur_node] = True
        for adj_node, length in adj_list[cur_node]:
            if not explored[adj_node]:
                dijkstra_gs = cur_dist + length #dijkstra's greedy score
                if dijkstra_gs < dist[adj_node]:
                    dist[adj_node] = dijkstra_gs
                    heapq.heappush(queue, (dijkstra_gs, adj_node))

    #give all unexplored nodes a distance of -1
    for node_num, state in explored.items():
        if state == False:
            dist[node_num] = -1

    #delete starting node distance from dictionary
    del dist[s]

    return list(dist.values())


if __name__ == '__main__':
    with open('dijkstra_input.txt', 'r') as input_f:
        t = int(input_f.readline())

        for t_itr in range(t):
            nm = input_f.readline().split()

            n = int(nm[0])

            m = int(nm[1])

            edges = []

            for _ in range(m):
                edges.append(list(map(int, input_f.readline().rstrip().split())))

            s = int(input_f.readline())

            result = shortestReach(n, edges, s)

            print(' '.join(map(str, result)))
            # print('\n')
