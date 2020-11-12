#!/usr/bin/env python3

import sys
import heapq
import collections

def read_graph(n):
    graph = collections.defaultdict(list)
    couples = {}
    for i in range(n):
        parents, children = sys.stdin.readline().strip().split(':')
        parent1, parent2 = parents.split()
        children = children.split()
        graph[parent1] = children
        graph[parent2] = children
        couples[parent1] = parent2
        couples[parent2] = parent1

    return graph, couples

def main():
    n = int(sys.stdin.readline().strip())
    while(n != 0):
        # try:
        graph, couples = read_graph(n)
        gifters = int(sys.stdin.readline().strip())
        for i in range(gifters):
            gifts = []
            gifter = sys.stdin.readline().strip()
            for person in graph.keys():
                if gifter in couples:
                    if gifter in graph[person] or couples[gifter] in graph[person]:
                        for parent in graph[person]:
                            if parent != gifter and parent != couples[gifter] and parent in graph:
                                gifts.extend(graph[parent])
                else:
                    if gifter in graph[person]:
                        for parent in graph[person]:
                            if parent != gifter:
                                gifts.extend(graph[parent])

            for children in graph[gifter]:
                if children in graph:
                    gifts = [];
                    break
            if gifts:
                print(gifter + " needs to buy gifts for: " + ", ".join(sorted(list(set(gifts)))))
            else:
                print(gifter + " does not need to buy gifts")

        n = int(sys.stdin.readline().strip())


        #     visited = find_circuit(graph, source, destination, max_stops)
        #     if destination in visited:
        #         out = visited[destination][1]
        #     else:
        #         out = -1
        #
        #     print(out)
        #
        #
        #     source, destination, max_stops, edges = map(int, sys.stdin.readline().strip().split())
        # except ValueError:
        #     break


if __name__ == '__main__':
    main()
