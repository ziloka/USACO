"""
ID: your_id_here
LANG: PYTHON3
TASK: gift1
"""
inputFile = open("gift1.in", "r")
lines = inputFile.read().split('\n')
people = {}
numberOfPeople = int(lines[0]) # number of people
for i in range(1, numberOfPeople+1):
    people[lines[i]] = {
        'order': i,
        'wallet': 0
    }

for num in range(numberOfPeople+1, len(lines)):
    line = lines[num].split(' ')
    if line[0] != '0' and any(char.isdigit() for char in line[0]):
        giver = lines[num-1]
        amountOfMoney = int(line[0])
        numOfPeople = int(line[1])
        people[giver]['wallet'] -= amountOfMoney
        people[giver]['wallet'] += amountOfMoney % numOfPeople
        for person in range(num+2, num+numOfPeople+2):
            people[lines[person-1]]['wallet'] += amountOfMoney // numOfPeople
def sortFunc(e):
    return people[e]['order']
names = list(people.keys())
names.sort(key=sortFunc)
result = '\n'.join([f'{key} {people[key]["wallet"]}' for key in names])
outputFile = open('gift1.out', 'w')
outputFile.write(result + '\n')
outputFile.close()
