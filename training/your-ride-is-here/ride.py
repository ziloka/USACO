"""
ID: your_id_here
LANG: PYTHON3
TASK: ride
"""
import sys
import os 
str = "abcdefghijklmnopqrstuvwxyz".upper()

inputFile = open("ride.in", "r")
data = inputFile.read().split('\n')
inputFile.close()

comentSum = 1
for letter in data[0]:
    comentSum *= str.index(letter)+1

groupSum = 1
for letter in data[1]:
    groupSum *= str.index(letter)+1

result = 'GO' if comentSum % 47 == groupSum % 47 else 'STAY'
outputFile = open('ride.out', 'a')
outputFile.write(result + '\n')
outputFile.close()
