#!/usr/bin/env python3

import sys
import heapq
import collections

def read_graph(edges):
    graph = collections.defaultdict(dict)

    for i in range(edges):
        edge = sys.stdin.readline().strip()
        s, t, weight = map(int, edge.split())
        graph[s][t] = weight

    return graph

def find_circuit(g, start, destination, max_stops):
    frontier = []
    visited  = {}

    heapq.heappush(frontier, (0, 0, start, start))

    while frontier:
        weight, stops, source, target = heapq.heappop(frontier)

        if target in visited or (destination != target and stops > max_stops):
            continue

        visited[target] = (source, weight, stops)

        for neighbor, cost in g[target].items():
            heapq.heappush(frontier, (weight + cost, stops + 1, target, neighbor))
    return visited


def main():
    source, destination, max_stops, edges = map(int, sys.stdin.readline().strip().split())
    while(True):
        try:
            graph = read_graph(edges)

            visited = find_circuit(graph, source, destination, max_stops)
            if destination in visited:
                out = visited[destination][1]
            else:
                out = -1

            print(out)


            source, destination, max_stops, edges = map(int, sys.stdin.readline().strip().split())
        except ValueError:
            break

if __name__ == '__main__':
    main()
