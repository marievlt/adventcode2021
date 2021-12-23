#!/usr/bin/env python3

# --- Part Two ---
# 
# Now that you have the structure of your transmission decoded, you can calculate the value of the expression it represents.
# 
# Literal values (type ID 4) represent a single number as described above. The remaining type IDs are more interesting:
# 
#     Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
#     Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
#     Packets with type ID 2 are minimum packets - their value is the minimum of the values of their sub-packets.
#     Packets with type ID 3 are maximum packets - their value is the maximum of the values of their sub-packets.
#     Packets with type ID 5 are greater than packets - their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
#     Packets with type ID 6 are less than packets - their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
#     Packets with type ID 7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
# 
# Using these rules, you can now work out the value of the outermost packet in your BITS transmission.
# 
# For example:
# 
#     C200B40A82 finds the sum of 1 and 2, resulting in the value 3.
#     04005AC33890 finds the product of 6 and 9, resulting in the value 54.
#     880086C3E88112 finds the minimum of 7, 8, and 9, resulting in the value 7.
#     CE00C43D881120 finds the maximum of 7, 8, and 9, resulting in the value 9.
#     D8005AC2A8F0 produces 1, because 5 is less than 15.
#     F600BC2D8F produces 0, because 5 is not greater than 15.
#     9C005AC2F8F0 produces 0, because 5 is not equal to 15.
#     9C0141080250320F1802104A08 produces 1, because 1 + 3 = 2 * 2.
# 
# What do you get if you evaluate the expression represented by your hexadecimal-encoded BITS transmission?


import numpy as np
from string import *

def main():
    file = open("input.txt", 'r')
    lines = file.readlines()

    hexadecimal = lines[0].strip()
    nb_of_bits  = 4*len(hexadecimal)
    packet      = bin(int(hexadecimal, 16))[2:].zfill(nb_of_bits)

    version, current_length, value = get_packet_version(packet)
    print ("\nTotal versions = ", version)
    print ("Total length = ", current_length)
    print ("Final value = ", value)
    return version


def get_packet_version(packet):
    version         = int(packet[0:3], 2)
    type_id         = int(packet[3:6], 2)
    current_length  = 6

    # Literal value packet
    if (type_id == 4):
        last = False
        datas = packet[6:]
        literal_value = ""
        i = 0
        while (last == False):
            if (datas[i*5] == '0'):
                last = True
            literal_value   += datas[i*5+1:i*5+5]
            current_length  += 5
            i+=1
        literal_value = int(literal_value, 2)
        operand = literal_value

    # Operator packet
    else:
        length_type     = packet[6]
        current_length += 1
        operands = []
        # Length type = number of bits
        if (length_type == '0'):
            length          = int(packet[7:22], 2)
            current_length  += 15
            version_t, current_length_t, operands = get_operator_0_versions(packet[22:], length)

        # Lenght type = number of subpackets
        else :
            nb_packets      = int(packet[7:18], 2)
            current_length  += 11
            version_t, current_length_t, operands = get_operator_1_versions(packet[18:], nb_packets)
        version += version_t
        current_length += current_length_t

        operand = do_operation(operands, type_id)

    #Return version for this packet and total bit length of this packet
    return version, current_length, operand


def get_operator_0_versions(packet, length):
    current_length = 0
    version = 0
    operands = []
    while (current_length < length) :
        version_t, current_length_t, operand = get_packet_version(packet[current_length:])
        version += version_t
        current_length+= current_length_t
        operands.append(operand)
    
    return version, current_length, operands

def get_operator_1_versions(packet, nb_packets):
    current_length = 0
    version = 0
    nb_subpackets = 0
    operands = []
    while (nb_subpackets < nb_packets):
        version_t, current_length_t, operand = get_packet_version(packet[current_length:])
        version += version_t
        current_length += current_length_t
        operands.append(operand)
        nb_subpackets+=1

    return version, current_length, operands

# 0 : SUM
# 1 : PRODUCT
# 2 : MINIMUM
# 3 : MAXIMUM
# 5 : GREATER THAN
# 6 : LESS THAN
# 7 : EQUAL TO
def do_operation(operands, type_id):
    if (type_id == 0):
        return sum(operands)
    elif (type_id == 1):
        product = 1
        for i in range(len(operands)):
            product *= operands[i]
        return product
    elif (type_id == 2):
        return min(operands)
    elif (type_id == 3):
        return max(operands)
    elif (type_id == 5):
        if (operands[0] > operands[1]):
            return 1
        else:
            return 0
    elif (type_id == 6):
        if (operands[0] < operands[1]):
            return 1
        else:
            return 0
    elif (type_id == 7):
        if (operands[0] == operands[1]):
            return 1
        else:
            return 0
    else:
        print ("ERROR, should never be there")
        exit()

main()    
