"""
ID: your_id_here
LANG: PYTHON3
TASK: beads
"""
inputFile = open('beads.in')
res = 0
n = int(inputFile.readline())
s = inputFile.readline().rstrip()
s = s + s

for i in range(0, n):
    c = s[i]
    current = 0
    j = i
    for state in range(1 if c != 'w' else 0, 3):
        while j < n + i and (s[j] == c or s[j] == 'w'):
            current+=1
            j+=1
        c = s[j]
    res = max(res, current)
outputFile = open('beads.out', 'w')
outputFile.write(str(res) + '\n')
outputFile.close()
