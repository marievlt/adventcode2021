#!/usr/bin/env python3


#--- Part Two ---
#
#The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair insertion process; a total of 40 steps should do it.
#
#In the above example, the most common element is B (occurring 2192039569602 times) and the least common element is H (occurring 3849876073 times); subtracting these produces 2188189693529.
#
#Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
#import numpy as np


# number of steps
N = 40

def main():
    file = open("input.txt", 'r')
    lines = file.readlines()

    template_polymer = lines[0].strip()
    pairs = {}
    for i in range (2, len(lines)):
        line = lines[i].strip().split(' -> ')
        key = line[0]
        value = line[1]
        pairs[key] = value


    count_pairs = {}
    for i in range (0, len(template_polymer)-1):
        current_pair = template_polymer[i]+template_polymer[i+1]
        if (current_pair in pairs):
            if (current_pair in count_pairs):
                count_pairs[current_pair] +=1
            else:
                count_pairs[current_pair] = 1

    for n in range(N):
        count_pairs = insert_pairs(count_pairs, pairs)

    res = calcul_quantity(count_pairs)
    print(res)
    return res


def insert_pairs(count_pairs, pairs):
    new_count_pairs = {}
    for item in count_pairs.items():
        if (item[0] in pairs):
            first_pair = item[0][0]+pairs[item[0]]
            second_pair = pairs[item[0]] + item[0][1]
            if (first_pair in new_count_pairs):
                new_count_pairs[first_pair] +=item[1]
            else:
                new_count_pairs[first_pair] = item[1]
            if (second_pair in new_count_pairs):
                new_count_pairs[second_pair] +=item[1]
            else:
                new_count_pairs[second_pair] = item[1]
    return new_count_pairs


def calcul_quantity(count_pairs):
    quantities = {}
    for item in count_pairs.items() :
        if (item[0][0] in quantities):
            quantities[item[0][0]] += item[1]
        else:
            quantities[item[0][0]] = item[1]
        if (item[0][1] in quantities):
            quantities[item[0][1]] += item[1]
        else:
            quantities[item[0][1]] = item[1]

    maximum = max(quantities.values())
    minimum = min(quantities.values())
    intermediate_res = maximum-minimum
    return (intermediate_res//2 + intermediate_res%2)
    

main()    
