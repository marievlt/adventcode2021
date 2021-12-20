#!/usr/bin/env python3

import numpy as np

def main():
    file = open("input.txt", 'r')
    lines = file.readlines()

    is_coord = True
    coords = []
    folds = []
    for line in lines :
        if not line.strip():
            is_coord = False
        else:
            if is_coord:
                l = line.strip().split(',')
                coords.append([l[0], l[1]])
            else:
                folds.append(line.split()[-1])

    grid        = create_grid(coords)
    new_grid    = fold_grid(grid, folds[0])

    print (np.sum(new_grid))
    return (np.sum(new_grid))
    
def create_grid(coords):
    nb_cols = 0
    nb_rows = 0
    for coord in coords:
        if (int(coord[0]) > nb_cols):
            nb_cols = int(coord[0])
            print (nb_cols)
        if (int(coord[1]) > nb_rows):
            nb_rows = int(coord[1])
    grid = np.zeros((nb_rows+1, nb_cols+1), dtype=bool)
    for coord in coords :
        grid[int(coord[1])][int(coord[0])] = True
    return grid

def fold_grid(grid, fold):
    direction, value = fold.split('=')
    value = int(value)

    if (direction == 'y'):
        first       = grid[:value, :]
        second      = np.flipud(grid[value+1:2*value+1 , :])
        new_grid    = np.logical_or(first, second)

    if (direction == 'x'):
        first       = grid[:, :value-1]
        second      = np.fliplr(grid[:, value+1:2*value])
        new_grid    = np.logical_or(first, second)
    
    return new_grid

main()    
