#!/usr/bin/env python3

## Problem 2F
## Mauricio Interiano and Pablo Martinez-Abrego

import sys
from collections import defaultdict

prereq_list = defaultdict(list)

# Check Dependancy of C2 on C1
def check_dependency(c1, c2):
    if c2 in prereq_list[c1]:
        print("Yes, {} is required for {}".format(c2, c1))
    else:
        print("No, {} is not required for {}".format(c2, c1))

# Add all courses to a list with dependancies
def add_courses(line):
    course, prereq = line.split(": ")
    for p in prereq.split():
        prereq_list[course].append(p)
        if prereq in prereq_list:
            for c in prereq_list[prereq]:
                prereq_list[course].append(c)


# Main Execution
def main():
    num = sys.stdin.readline().rstrip()
    while True:
        if not num:
            break
        lines = []
        for i in range(int(num)):
            lines.append(sys.stdin.readline().rstrip())

        # Iterate normally
        for line in lines:
            add_courses(line)
        # Iterate backwards
        i = len(lines) - 1
        while i >= 0:
            add_courses(lines[i])
            i -= 1

        # Read queries
        num = int(sys.stdin.readline().rstrip())
        for i in range(num):
            c1, c2 = sys.stdin.readline().rstrip().split()
            check_dependency(c1, c2)
        num = sys.stdin.readline().rstrip()
        if not num:
            break;
        else:
            print()

# Main Execution
if __name__ == '__main__':
    main()
