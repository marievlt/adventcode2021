#!/usr/bin/env python3

#--- Part Two ---
#
#Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?
#
#After 256 days in the example above, there would be a total of 26984457539 lanternfish!
#
#How many lanternfish would there be after 256 days?


import numpy as np

N = 256

def main():
    file = open("input.txt", 'r')
    lines = file.readlines()

    lanternfishes_init = [int(i) for i in lines[0].strip().split(',')]

    lanternfishes_nb = np.zeros(9, dtype=int)
    for i in lanternfishes_init:
        if (lanternfishes_init[i] > 8):
            print ("ERROR : a lanternfish cannot have an internal counter > 8")
            exit()
        elif (lanternfishes_init[i] < 0):
            print ("ERROR : a lanternship cannot have a negatve internal counter")
            exit()
        else:
            lanternfishes_nb[i]+=1;

    for i in range(N):
        lanternfishes_nb = next_day(lanternfishes_nb)

    print ("Number of lanternfishes = ", np.sum(lanternfishes_nb))

def next_day(array):
    new = array[0]
    for i in range(8):
        array[i] = array[i+1]
    array[8] = new
    array[6] += new
    return array


main()    
