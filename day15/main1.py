#!/usr/bin/env python3

#--- Day 15: Chiton ---
#
#You've almost reached the exit of the cave, but the walls are getting closer together. Your submarine can barely still fit, though; the main problem is that the walls of the cave are covered in chitons, and it would be best not to bump any of them.
#
#The cavern is large, but has a very low ceiling, restricting your motion to two dimensions. The shape of the cavern resembles a square; a quick scan of chiton density produces a map of risk level throughout the cave (your puzzle input). For example:
#
#1163751742
#1381373672
#2136511328
#3694931569
#7463417111
#1319128137
#1359912421
#3125421639
#1293138521
#2311944581
#
#You start in the top left position, your destination is the bottom right position, and you cannot move diagonally. The number at each position is its risk level; to determine the total risk of an entire path, add up the risk levels of each position you enter (that is, don't count the risk level of your starting position unless you enter it; leaving it adds no risk to your total).
#
#Your goal is to find a path with the lowest total risk. In this example, a path with the lowest total risk is highlighted here:
#
#1163751742
#1381373672
#2136511328
#3694931569
#7463417111
#1319128137
#1359912421
#3125421639
#1293138521
#2311944581
#
#The total risk of this path is 40 (the starting position is never entered, so its risk is not counted).
#
#What is the lowest total risk of any path from the top left to the bottom right?

import numpy as np

def main():
    file = open("input.txt", 'r')
    lines = file.readlines()

    risk_map = np.zeros((len(lines), len (lines[0].strip())), dtype=int)
    for i in range(len(lines)):
        for j in range(len(lines[0].strip())):
            risk_map[i][j] = int(lines[i][j])

    res = find_lower_risk_path(risk_map)
    print (res)
    return res


def find_lower_risk_path(risk_map):
    pos = (0, 0)
    final = (len(risk_map)-1, len(risk_map[0])-1)
    total = 0

    while (pos != final):
        if (pos[0] == len(risk_map)-1):
            next_pos = (pos[0], pos[1]+1)
        elif (pos[1] == len(risk_map[0])-1):
            next_pos = (pos[0]+1, pos[1])
        else:
            if (risk_map[pos[0]+1][pos[1]] >= risk_map[pos[0]][pos[1]+1]):
                next_pos = (pos[0], pos[1]+1)
            else:
                next_pos = (pos[0]+1, pos[1])

        total += risk_map[next_pos[0], next_pos[1]]
        pos = next_pos

    return total




main()    
