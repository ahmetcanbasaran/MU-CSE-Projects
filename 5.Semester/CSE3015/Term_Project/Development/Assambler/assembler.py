<<<<<<< HEAD:Development/assembler.py
#!/usr/bin/python

import sys
import os
import os.path

'''
Digital Logic Design Term Project
Assambler
Yusuf Kamil AK -> 150116827
Oguzhan BOLUKBAS -> 150114022
Bilgehan NAL -> 150114---
'''

# MARK : CONVERSION

def decToBinary(n, bit):
    '''Returns the string with the binary representation of non-negative integer n.'''
    result = ''
    for x in range(bit):
        r = n % 2
        n = n // 2
        result += str(r)

    result = result[::-1]
    return result

def numToTc(n, bit):
    '''Returns the string with the binary representation of non-negative integer n.'''
    binary = decToBinary(n, bit)
    for digit in binary:
        if int(digit) < 0:
            binary = (1 << bit) + n
    return binary

# MARK : InstructionPrecedures

# BEQ -> 0100
def instructionBeq(assemb):
    return '0100' + numToTc(int(assemb[0][1:]), 4) \
    + numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2]), 8)

# BLT -> 1000
def instructionBlt(assemb):
    return '1000' + numToTc(int(assemb[0][1:]), 4) \
    + numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2]), 8)

# BGT -> 0010
def instructionBgt(assemb):
    return '0010' + numToTc(int(assemb[0][1:]), 4) \
    + numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2]), 8)

# BLE -> 1100
def instructionBle(assemb):
    return '1100' + numToTc(int(assemb[0][1:]), 4) \
    + numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2]), 8)

# BGE -> 0110
def instructionBge(assemb):
    return '0110' + numToTc(int(assemb[0][1:]), 4) \
+ numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2]), 8)

# ADD -> 0000
def instructionAdd(assemb):
    return '0000' + numToTc(int(assemb[0][1:]), 4) \
    + numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2][1:]), 4) \
    + numToTc(0, 4)

# ADDI -> 0001
def instructionAddi(assemb):
    return '0001' + numToTc(int(assemb[0][1:]), 4) \
    + numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2]), 8)

# AND -> 1010
def instructionAnd(assemb):
    return '1010' + numToTc(int(assemb[0][1:]), 4) \
    + numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2][1:]), 4) \
    + numToTc(0, 4)

# ANDI -> 1011
def instructionAndi(assemb):
    return '1011' + numToTc(int(assemb[0][1:]), 4) \
    + numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2]), 8)

# OR -> 1110
def instructionOr(assemb):
    return '1110' + numToTc(int(assemb[0][1:]), 4) \
    + numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2][1:]), 4) \
    + numToTc(0, 4)

# ORI -> 1111
def instructionOri(assemb):
    return '1111' + numToTc(int(assemb[0][1:]), 4) \
    + numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2]), 8)

# XOR -> 0101
def instructionXor(assemb):
    return '0101' + numToTc(int(assemb[0][1:]), 4) \
    + numToTc(int(assemb[1][1:]), 4) \
    + numToTc(int(assemb[2][1:]), 4) + '0000'

# XORI -> 1001
def instructionXori(assemb):
    return '1001' + numToTc(int(assemb[0][1:]), 4) \
    + numToTc(int(assemb[1][1:]), 4) \
    + numToTc(int(assemb[2]), 8)

# JUMP -> 0011
def instructionJmp(assemb):
    return '0011' + numToTc(int(assemb[0]), 16)

# LD -> 1101
def instructionLd(assemb):
    return '1101' + numToTc(int(assemb[0][1:]), 4) + numToTc(int(assemb[1]), 12)

# ST -> 0111
def instructionSt(assemb):
    return '0111' + numToTc(int(assemb[0][1:]), 4) + numToTc(int(assemb[1]), 12)

# MARK : InstructionTable
# This table keeps procedures according to key of their oppcodes.
instructionTable = {
    'BEQ' : instructionBeq,
    'BLT' : instructionBlt,
    'BGT' : instructionBgt,
    'BLE' : instructionBle,
    'BGE' : instructionBge,
    'ADD' : instructionAdd,
    'ADDI' : instructionAddi,
    'AND' : instructionAnd,
    'ANDI' : instructionAndi,
    'OR' : instructionOr,
    'ORI' : instructionOri,
    'XOR' : instructionXor,
    'XORI' : instructionXori,
    'JUMP' : instructionJmp,
    'LD' : instructionLd,
    'ST' : instructionSt
}

# MARK : I/O

def readFile(fileName) :
    with open(fileName, 'r') as content_file:
        content = content_file.read()
        return content
    return 'none'

def writeFile(fileName, string) :
    if os.path.exists(fileName) :
        os.remove(fileName)
    file = open(fileName,'w')
    for element in string:
        file.write(str(element))
        file.write('\n')
    file.close()

# MARK : Main

def main(argv) :

    # Assambly Codes are taken from the given file.
    inputs = readFile(argv[0])
    inputs = inputs.split("\n")

    #Results writting to output file
    outputFileName = argv[1]
    listOfOutputs = []

    for theAssemblyCode in inputs :
        theAssemblyCode = theAssemblyCode.split(" ")
        instruction = theAssemblyCode[0]
        machineCode = instructionTable[instruction](theAssemblyCode[1].split(",")) # Machine code taken from the instruction function
        listOfOutputs.append(machineCode)

    writeFile(outputFileName, listOfOutputs)

if __name__ == "__main__":
   main(sys.argv[1:])
=======
#!/usr/bin/python

import sys
import os
import os.path

'''
Digital Logic Design Term Project
Assambler
Yusuf Kamil AK -> 150116827
Oguzhan BOLUKBAS -> 150114022
Bilgehan NAL -> 150114---
'''

# MARK : CONVERSION

def decToBinary(n, bit):
    '''Returns the string with the binary representation of non-negative integer n.'''
    result = ''
    for x in range(bit):
        r = n % 2
        n = n // 2
        result += str(r)

    result = result[::-1]
    return result

def numToTc(n, bit):
    '''Returns the string with the binary representation of non-negative integer n.'''
    binary = decToBinary(n, bit)
    for digit in binary:
        if int(digit) < 0:
            binary = (1 << bit) + n
    return binary

# MARK : InstructionPrecedures

# BEQ -> 0100
def instructionBeq(assemb):
    return '0100' + numToTc(int(assemb[0][1:]), 4) \
    + numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2]), 8)

# BLT -> 1000
def instructionBlt(assemb):
    return '1000' + numToTc(int(assemb[0][1:]), 4) \
    + numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2]), 8)

# BGT -> 0010
def instructionBgt(assemb):
    return '0010' + numToTc(int(assemb[0][1:]), 4) \
    + numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2]), 8)

# BLE -> 1100
def instructionBle(assemb):
    return '1100' + numToTc(int(assemb[0][1:]), 4) \
    + numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2]), 8)

# BGE -> 0110
def instructionBge(assemb):
    return '0110' + numToTc(int(assemb[0][1:]), 4) \
+ numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2]), 8)

# ADD -> 0000
def instructionAdd(assemb):
    return '0000' + numToTc(int(assemb[0][1:]), 4) \
+ numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2][1:]), 4) \
+ numToTc(0, 4)

# ADDI -> 0001
def instructionAddi(assemb):
    return '0001' + numToTc(int(assemb[0][1:]), 4) \
+ numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2]), 8)

# AND -> 1010
def instructionAnd(assemb):
    return '1010' + numToTc(int(assemb[0][1:]), 4) \
+ numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2][1:]), 4) \
+ numToTc(0, 4)

# ANDI -> 1011
def instructionAndi(assemb):
    return '1011' + numToTc(int(assemb[0][1:]), 4) \
+ numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2]), 8)

# OR -> 1110
def instructionOr(assemb):
    return '1110' + numToTc(int(assemb[0][1:]), 4) \
+ numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2][1:]), 4) \
+ numToTc(0, 4)

# ORI -> 1111
def instructionOri(assemb):
    return '1111' + numToTc(int(assemb[0][1:]), 4) \
+ numToTc(int(assemb[1][1:]), 4) + numToTc(int(assemb[2]), 8)

# XOR -> 0101
def instructionXor(assemb):
    return '0101' + numToTc(int(assemb[0][1:]), 4) + \
        numToTc(int(assemb[1][1:]), 4) + \
        numToTc(int(assemb[2][1:]), 4) + '0000'

# XORI -> 1001
def instructionXori(assemb):
    return '1001' + numToTc(int(assemb[0][1:]), 4) + \
    numToTc(int(assemb[1][1:]), 4) + \
    numToTc(int(assemb[2]), 8)

# JUMP -> 0011
def instructionJmp(assemb):
    return '0011' + numToTc(int(assemb[0]), 16)

# LD -> 1101
def instructionLd(assemb):
    return '1101' + numToTc(int(assemb[0][1:]), 4) + numToTc(int(assemb[1]), 12)

# ST -> 0111
def instructionSt(assemb):
    return '0111' + numToTc(int(assemb[0][1:]), 4) + numToTc(int(assemb[1]), 12)

# MARK : InstructionTable
# This table keeps procedures according to key of their oppcodes.
instructionTable = {
    'BEQ' : instructionBeq,
    'BLT' : instructionBlt,
    'BGT' : instructionBgt,
    'BLE' : instructionBle,
    'BGE' : instructionBge,
    'ADD' : instructionAdd,
    'ADDI' : instructionAddi,
    'AND' : instructionAnd,
    'ANDI' : instructionAndi,
    'OR' : instructionOr,
    'ORI' : instructionOri,
    'XOR' : instructionXor,
    'XORI' : instructionXori,
    'JUMP' : instructionJmp,
    'LD' : instructionLd,
    'ST' : instructionSt
}

binaryToHexTable = {
    '0000' : '0',
    '0001' : '1',
    '0010' : '2',
    '0011' : '3',
    '0100' : '4',
    '0101' : '5',
    '0110' : '6',
    '0111' : '7',
    '1000' : '8',
    '1001' : '9',
    '1010' : 'a',
    '1011' : 'b',
    '1100' : 'c',
    '1101' : 'd',
    '1110' : 'e',
    '1111' : 'f'
}

# MARK : I/O

def readFile(fileName) :
    with open(fileName, 'r') as content_file:
        content = content_file.read()
        return content
    return 'none'

def binToHex(binaryValue):
    return binaryToHexTable[binaryValue[0:4]] + binaryToHexTable[binaryValue[4:8]] + \
    binaryToHexTable[binaryValue[8:12]] + \
    binaryToHexTable[binaryValue[12:16]] + \
    binaryToHexTable[binaryValue[16:20]]

def writeFileBin(fileName, string) :
    if os.path.exists(fileName) :
        os.remove(fileName)
    file = open(fileName,'w')
    for element in string:
        file.write(str(element))
        file.write('\n')
    file.close()

def writeFileHex(fileName, string) :
    if os.path.exists(fileName) :
        os.remove(fileName)
    file = open(fileName,'w')
    file.write("v2.0 raw\n")
    for element in string:
        file.write(str(binToHex(element)))
        file.write(' ')
    file.close()

# MARK : Main

def main(argv) :

    # Assambly Codes are taken from the given file.
    inputs = readFile(argv[0])
    inputs = inputs.split("\n")

    #Results writting to output file
    outputFileNameHex = argv[1]
    outputFileNameBin = argv[2]
    listOfOutputs = []

    for theAssemblyCode in inputs :
        theAssemblyCode = theAssemblyCode.split(" ")
        instruction = theAssemblyCode[0]
        machineCode = instructionTable[instruction](theAssemblyCode[1].split(",")) # Machine code taken from the instruction function
        listOfOutputs.append(machineCode)

    writeFileBin(outputFileNameBin, listOfOutputs)
    writeFileHex(outputFileNameHex, listOfOutputs)

if __name__ == "__main__":
   main(sys.argv[1:])
>>>>>>> fd7bcde26b405b41d259afbba6d5cd33ad6c6b39:Development/Assambler/assembler.py
