#!/usr/bin/env python3

import sys

class Node:
    def __init__(self, data):
        self.val = data
        self.left = self.right = None

def read_tree(nodes, i):
    if i > len(nodes)-1:
        return None

    root = Node(nodes[i])

    root.left = read_tree(nodes, 2*i + 1)
    root.right = read_tree(nodes, 2*i + 2)

    return root

def find_slant(root, slant):
    if not root:
        return 0

    left = find_slant(root.left, slant)
    right = find_slant(root.right, slant)

    slant[0] += abs(left - right)

    return left + right + root.val

def slanted(root):
    slant = [0]
    find_slant(root, slant)
    return slant[0]

def main():
    for line in sys.stdin:
        nodes = list(map(int, line.split()))
        root = read_tree(nodes, 0)
        print(slanted(root))

if __name__ == '__main__':
    main()
