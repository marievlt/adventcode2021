#!/usr/bin/env python3

#--- Part Two ---
#
#On the other hand, it might be wise to try a different strategy: let the giant squid win.
#
#You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.
#
#In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.
#
#Figure out which board will win last. Once it wins, what would its final score be?


import numpy as np

# Bingo grid width
N = 5

def main():
    file = open("input.txt", 'r')
    lines = file.readlines()

    choosen_nbs = (lines[0].strip()).split(',')
    lines.pop(0)
    grids_nbs = int(len(lines)/(N+1))

    grids = np.zeros((grids_nbs, N, N), dtype=int)
    hits = np.zeros((grids_nbs, N, N), dtype=int)
    ranking = []

    for i in range(grids_nbs):
        for j in range (N):
            values = (lines[(N+1)*i+1+j].strip()).split()
            for k in range(N):
                grids[i][j][k] = int(values[k])


    for number in choosen_nbs:
        find_position = np.where(grids == int(number))
        for i in range(len(find_position[0])):
            hits[find_position[0][i]][find_position[1][i]][find_position[2][i]] = 1
            if (is_bingo(hits[find_position[0][i]]) == True):
                if (find_position[0][i] not in ranking):
                    ranking.append(find_position[0][i])
            if (grids_nbs == len(ranking)):
                result = score(grids[ranking[-1]], hits[ranking[-1]], number)
                return result


def is_bingo(grid):
    sum_line = (np.sum(grid, axis=0))
    sum_column = (np.sum(grid, axis=1))
    for i in range(N):
        if (sum_line[i] == N or sum_column[i] == N):
            return True
    return False

def score(grid, hits, number):
    score = 0
    for i in range(N):
        for j in range(N):
            if (hits[i][j] == 0):
                score += grid[i][j]
    print (score)
    print (number)
    return score*number


main()
    
