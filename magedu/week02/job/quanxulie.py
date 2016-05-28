#!/usr/bin/env python

matrix = [[x, y, z] for x in range(1, 4) for y in range(1, 4)  for z in range(1, 4) if y != x and y != z and x != z ]

print(matrix)
print('-' * 40)

for x in range(1, 4):
    for y in range(1, 4):
        for z in range(1, 4):
            if y != x and y != z and x != z:
                print(x, y, z)
