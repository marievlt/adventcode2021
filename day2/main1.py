#!/usr/bin/env python3

def main():
    file = open('input.txt', 'r')
    lines = file.readlines()

    horizontal = 0
    depth = 0

    for line in lines :
        if (line.split()[0] == 'forward'):
            horizontal = horizontal + int(line.split()[1])
        elif (line.split()[0] == 'down'):
            depth = depth + int(line.split()[1])
        elif (line.split()[0] == 'up'):
            depth = depth - int(line.split()[1])
        else :
            print ("Match case not found")

    print ("horizontal = ", horizontal)
    print ("depth = ", depth)
    print ("product = ", horizontal*depth)


main()
    
