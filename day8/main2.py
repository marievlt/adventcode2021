#!/usr/bin/env python3

# --- Part Two ---
# 
# Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:
# 
# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
# cdfeb fcadb cdfeb cdbaf
# 
# After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:
# 
#  dddd
# e    a
# e    a
#  ffff
# g    b
# g    b
#  cccc
# 
# So, the unique signal patterns would correspond to the following digits:
# 
#     acedgfb: 8
#     cdfbe: 5
#     gcdfa: 2
#     fbcad: 3
#     dab: 7
#     cefabd: 9
#     cdfgeb: 6
#     eafb: 4
#     cagedb: 0
#     ab: 1
# 
# Then, the four digits of the output value can be decoded:
# 
#     cdfeb: 5
#     fcadb: 3
#     cdfeb: 5
#     cdbaf: 3
# 
# Therefore, the output value for this entry is 5353.
# 
# Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:
# 
#     fdgacbe cefdb cefbgd gcbe: 8394
#     fcgedb cgb dgebacf gc: 9781
#     cg cg fdcagb cbg: 1197
#     efabcd cedba gadfec cb: 9361
#     gecf egdcabf bgf bfgea: 4873
#     gebdcfa ecba ca fadegcb: 8418
#     cefg dcbef fcge gbcadfe: 4548
#     ed bcgafe cdgba cbgef: 1625
#     gbdfcae bgc cg cgb: 8717
#     fgae cfgab fg bagce: 4315
# 
# Adding all of the output values in this larger example produces 61229.
# 
# For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?


import numpy as np

def main():
    file = open("input.txt", 'r')
    lines = file.readlines()

    one_segments_nb     = 2
    four_segments_nb    = 4
    seven_segments_nb   = 3
    eight_segments_nb   = 7
    sum_digits=0

    inputs  = ['z']*len(lines)
    outputs = ['z']*len(lines)

    for i in range (len(lines)):
        inputs[i], outputs[i] = ((lines[i].strip()).split('|'))
        outputs[i] = outputs[i].lstrip()

    for output in outputs:
        digits = output.split()
        for digit in digits:
            if ((len(digit) == one_segments_nb) or
                (len(digit) == four_segments_nb) or
                (len(digit) == seven_segments_nb) or
                (len(digit) == eight_segments_nb)):
                    sum_digits+=1

    print(sum_digits)


main()    
