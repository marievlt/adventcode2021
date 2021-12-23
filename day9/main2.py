#!/usr/bin/env python3

# --- Part Two ---
# 
# Next, you need to find the largest basins so you know what areas are most important to avoid.
# 
# A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.
# 
# The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.
# 
# The top-left basin, size 3:
# 
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# 
# The top-right basin, size 9:
# 
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# 
# The middle basin, size 14:
# 
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# 
# The bottom-right basin, size 9:
# 
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# 
# Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.
# 
# What do you get if you multiply together the sizes of the three largest basins?


import numpy as np

def main():
    file = open("toto", 'r')
    lines = file.readlines()

    line        = len(lines)
    col         = len(lines[0].strip())
    lowpoints   = []
    basin_size = []

    array = np.zeros((line, col), dtype=int)
    for i in range(line):
        lines[i] = lines[i].strip()
        for j in range(col):
            array[i][j] = int(lines[i][j])

    array = np.insert(array, col,  [9]*line, axis=1)
    array = np.insert(array, 0,    [9]*line, axis=1)
    array = np.insert(array, line, [9]*(col+2), axis=0)
    array = np.insert(array, 0,    [9]*(col+2), axis=0)

    for i in range(line):
        for j in range(col):
            if (is_lowpoint(array, i+1, j+1) != 9):
                lowpoints.append((i+1, j+1))

    for coord in lowpoints:
        print ("lowpoint tested : ", coord)
        size = is_basin(array, coord[0], coord[1], 0)
        basin_size.append(size)
        print ("basin size = ", size)

    basin_size = sorted(basin_size)
    print (basin_size[-1]*basin_size[-2]*basin_size[-3])



def is_lowpoint(array, i, j):
    minimum = array[i][j]
    if ((array[i-1][j] <= minimum) or (array[i+1][j] <= minimum) or (array[i][j-1] <= minimum) or (array[i][j+1] <= minimum)):
        return 9
    else :
        return minimum


def is_basin(array, x, y, size):
    if (array[x][y+1] != 9):
        is_basin(array, x, y+1, size)
        size += 1
    if (array[x][y-1] != 9):
        is_basin(array, x, y-1, size)
        size += 1
    if (array[x+1][y] != 9):
        is_basin(array, x+1, y, size)
        size += 1
    if (array[x-1][y] != 9):
        is_basin(array, x-1, y, size)
        size += 1
    return size

main()    
