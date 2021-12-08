#!/usr/bin/env python3

# --- Part Two ---
# 
# Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.
# 
# Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:
# 
#     An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
#     An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
# 
# Considering all lines from the above example would now produce the following diagram:
# 
# 1.1....11.
# .111...2..
# ..2.1.111.
# ...1.2.2..
# .112313211
# ...1.2....
# ..1...1...
# .1.....1..
# 1.......1.
# 222111....
# 
# You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.
# 
# Consider all of the lines. At how many points do at least two lines overlap?


import numpy as np

# Window size
N = 1000

def main():
    file = open("input.txt", 'r')
    lines = file.readlines()

    diagram = np.zeros((N, N), dtype=int)

    for line in lines:
        x1, y1 = ((line.split())[0]).split(',')
        x2, y2 = ((line.split())[2]).split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int (y1), int(y2)

        xmin = min(x1, x2)
        xmax = max(x1, x2)
        ymin = min(y1, y2)
        ymax = max(y1, y2)

        if (x1 == x2):
            for i in range (ymin, ymax+1):
                diagram[x1][i]+=1;
        elif (y1 == y2):
            for i in range (xmin, xmax+1):
                diagram[i][y1]+=1;
        else:
            i = xmax
            if (xmax == x1):
                j = y1
            else :
                j = y2
            if (j == ymin):
                increment = 1
            else:
                increment = -1
            while (i >= xmin):
                diagram[i][j]+=1
                i-=1
                j+=increment

    print (nb_points_to_avoid(diagram))

def nb_points_to_avoid(diagram):
    nb = 0
    for i in range(N):
        for j in range(N):
            if (diagram[i][j] >= 2):
                nb+=1
    return nb


main()    
