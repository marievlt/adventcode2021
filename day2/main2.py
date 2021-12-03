#!/usr/bin/env python3

def main():
    file = open('input.txt', 'r')
    lines = file.readlines()

    horizontal = 0
    depth = 0
    aim = 0

    for line in lines :
        if (line.split()[0] == 'forward'):
            horizontal = horizontal + int(line.split()[1])
            depth = depth + aim*int(line.split()[1])
        elif (line.split()[0] == 'down'):
            aim = aim + int(line.split()[1])
        elif (line.split()[0] == 'up'):
            aim = aim - int(line.split()[1])
        else :
            print ("Match case not found")

    print ("horizontal = ", horizontal)
    print ("depth = ", depth)
    print ("product = ", horizontal*depth)


main()
    
