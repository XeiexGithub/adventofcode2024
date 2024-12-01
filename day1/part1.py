#!/bin/py

left = []
right = []
final = []

with open('input.txt', 'r') as f:
    input = f.readlines()
    for line in input:
        left.append(line.split("  ")[0])
        right.append(line.split("  ")[1].strip())

leftSorted = list(map(int, sorted(left)))
rightSorted = list(map(int, sorted(right)))

for i in range(len(leftSorted)):
    final.append(abs(leftSorted[i] - rightSorted[i]))

ans = sum(final)
print(ans)