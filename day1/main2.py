#!/usr/bin/env python3

def main():
    file = open('input.txt', 'r')
    lines = file.readlines()
    report = []
    average_report = []

    for measure in lines:
        report.append(int(measure))

    if (len(report) < 3):
        print ("No enough measures")
        exit()

    for i in range (0, len(report)-2):
        average_report.append(report[i] + report[i+1] + report[i+2])

    sum_inc = 0
    for i in range(1, len(average_report)):
        if (average_report[i] > average_report[i-1]):
            sum_inc = sum_inc + 1

    print (sum_inc)


main()
    
