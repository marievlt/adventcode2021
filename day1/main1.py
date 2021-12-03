#!/usr/bin/env python3

def main():
    file = open('input.txt', 'r')
    lines = file.readlines()
    report = []

    for measure in lines:
        report.append(int(measure))

    sum_inc = 0
    for i in range(1, len(report)):
        if (report[i] > report[i-1]):
            sum_inc = sum_inc + 1

    print (sum_inc)


main()
    
