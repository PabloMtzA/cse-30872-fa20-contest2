#!/usr/bin/env python3

## Problem 2C
## Mauricio Interiano and Pablo Martinez-Abrego

import sys

# 1 After 2*Node is Left Child
def left_child(i):
    return i*2 + 1

# 2 After 2*Node is Right Child
def right_child(i):
    return i*2 + 2

# Recursively create paths and check if sum
def find_paths(tree, paths, i, curr_path):
    curr_path.append(tree[i])
    num_nodes = len(tree)

    # Base Case
    # No more Children and check if sum
    if (right_child(i) >= num_nodes or tree[right_child(i)] == 0)\
    and (left_child(i) >= num_nodes or tree[left_child(i)] == 0):
        if(sum(curr_path) == target):
            paths.append(curr_path)

    # Recursion
    # Go to left and right (if available)
    if (right_child(i) < num_nodes and tree[right_child(i)] != 0):
        find_paths(tree, paths, right_child(i), curr_path[:])
    if (left_child(i) < num_nodes and tree[left_child(i)] != 0):
        find_paths(tree, paths, left_child(i), curr_path[:])

    return 1

# Main Execution
def main():
    for line in sys.stdin:
        global target  # To avoid passing it every time in recursion
        target = int(line)
        tree = list(map(int, sys.stdin.readline().rsplit()))

        paths = []
        find_paths(tree, paths, 0, [])
        for path in sorted(paths):
            print(str(target) + ': ', end='')
            print(", ".join(map(str, path)))


# Main Execution
if __name__ == '__main__':
    main()
