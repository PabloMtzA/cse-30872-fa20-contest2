#!/usr/bin/env python3

## Problem 2A
## Mauricio Interiano and Pablo Martinez-Abrego

import sys
from collections import defaultdict

def read_graph():
    graph = defaultdict(list)
    try:
        vertices = int(sys.stdin.readline())
    except:
        return []
    edges = int(sys.stdin.readline())
    for i in range(1, vertices+1):
        graph[i] = []
    for _ in range(edges):
        source, target = map(int, sys.stdin.readline().rstrip().split())
        graph[source].append(target)
        graph[target].append(source)

    return graph

def search_graph(graph):
    search = []
    for i in graph.keys():
        visited = []
        queue = []
        queue.append(i)
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                for n in graph[node]:
                    queue.append(n)
        search.append(visited)

    for i in range(len(search)):
        search[i].sort()

    return search

def main():
    groupNum = 1
    while True:
        graph = read_graph()
        if not graph:
            break
        search = search_graph(graph)
        groups = []
        for i in search:
            if i not in groups:
                groups.append(i)

        if len(groups) == 1:
            print("Graph {} has 1 group:".format(groupNum))
        else:
            print("Graph {} has {} groups:".format(groupNum, len(groups)))
        for group in groups:
            group = [str(i) for i in group]
            print(' '.join(group))

        groupNum += 1

if __name__ == '__main__':
    main()
