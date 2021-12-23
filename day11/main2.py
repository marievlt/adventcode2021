#!/usr/bin/env python3

# --- Part Two ---
# 
# Now, discard the corrupted lines. The remaining lines are incomplete.
# 
# Incomplete lines don't have any incorrect characters - instead, they're missing some closing characters at the end of the line. To repair the navigation subsystem, you just need to figure out the sequence of closing characters that complete all open chunks in the line.
# 
# You can only use closing characters (), ], }, or >), and you must add them in the correct order so that only legal pairs are formed and all chunks end up closed.
# 
# In the example above, there are five incomplete lines:
# 
#     [({(<(())[]>[[{[]{<()<>> - Complete by adding }}]])})].
#     [(()[<>])]({[<{<<[]>>( - Complete by adding )}>]}).
#     (((({<>}<{<{<>}{[]{[]{} - Complete by adding }}>}>)))).
#     {<[[]]>}<{[{[{[]{()[[[] - Complete by adding ]]}}]}]}>.
#     <{([{{}}[<[[[<>{}]]]>[]] - Complete by adding ])}>.
# 
# Did you know that autocomplete tools also have contests? It's true! The score is determined by considering the completion string character-by-character. Start with a total score of 0. Then, for each character, multiply the total score by 5 and then increase the total score by the point value given for the character in the following table:
# 
#     ): 1 point.
#     ]: 2 points.
#     }: 3 points.
#     >: 4 points.
# 
# So, the last completion string above - ])}> - would be scored as follows:
# 
#     Start with a total score of 0.
#     Multiply the total score by 5 to get 0, then add the value of ] (2) to get a new total score of 2.
#     Multiply the total score by 5 to get 10, then add the value of ) (1) to get a new total score of 11.
#     Multiply the total score by 5 to get 55, then add the value of } (3) to get a new total score of 58.
#     Multiply the total score by 5 to get 290, then add the value of > (4) to get a new total score of 294.
# 
# The five lines' completion strings have total scores as follows:
# 
#     }}]])})] - 288957 total points.
#     )}>]}) - 5566 total points.
#     }}>}>)))) - 1480781 total points.
#     ]]}}]}]}> - 995444 total points.
#     ])}> - 294 total points.
# 
# Autocomplete tools are an odd bunch: the winner is found by sorting all of the scores and then taking the middle score. (There will always be an odd number of scores to consider.) In this example, the middle score is 288957 because there are the same number of scores smaller and larger than it.
# 
# Find the completion string for each incomplete line, score the completion strings, and sort the scores. What is the middle score?


import numpy as np

def main():
    file = open("input.txt", 'r')
    lines = file.readlines()

    open_chunk_list     = ['(', '{', '[', '<']
    close_chunk_list    = [')', '}', ']', '>']
    corrupted_line      = []
    incomplete_line     = []
    complete_line       = []

    corrupted_score     = 0
    incomplete_score    = []

    for line in lines:
        line = line.strip()
        open_list = []
        corrupt = 0
        for index in range(len(line)):
            if (line[index] in open_chunk_list):
                open_list.append(line[index])
            else :
                if ((len(open_list) == 0) or (close_chunk_list.index(line[index]) != open_chunk_list.index(open_list[-1]))):
                    corrupted_line.append((line, index))
                    corrupt = 1
                    break
                else:
                    open_list.pop(-1)
        if (corrupt == 0):
            incomplete_line.append(open_list)

    for corrupt in corrupted_line:
        corrupted_score += calcul_corrupted_score(corrupt[0], corrupt[1])

    for incomplete in incomplete_line:
        string = ''
        while (len(incomplete) != 0):
            string += close_chunk_list[open_chunk_list.index(incomplete.pop())]
        complete_line.append(string)

    for complete in complete_line:
        incomplete_score.append(calcul_incomplete_score(complete))

    incomplete_score.sort()

    print (incomplete_score[int(len(incomplete_score)/2)])


def calcul_corrupted_score(line, position):
    if (line[position] == ')'):
        return 3
    elif (line[position] == ']'):
        return 57
    elif (line[position] == '}'):
        return 1197
    elif (line[position] == '>'):
        return 25137
    else:
        print("ERROR")
        return 0

def calcul_incomplete_score(line):
    score = 0
    for i in range(len(line)):
        score *= 5
        if (line[i] == ')'):
            score += 1
        elif (line[i] == ']'):
            score += 2
        elif (line[i] == '}'):
            score += 3
        elif (line[i] == '>'):
            score += 4
        else:
            print("ERROR")
    return score


main()    
