"""
ID: your_id_here
LANG: PYTHON3
TASK: friday
"""
# Do not use any built-in date functions in your computer language.
# Don't just precompute the answers, either, please.
def isLeap(year):
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0

with open('friday.in') as file:
    input = int(file.readline()) # num years

calendarDay = 0
freq = [0, 0, 0, 0, 0, 0, 0]
normDays = [31,28,31,30,31,30,31,31,30,31,30,31]
leapDays = [31,29,31,30,31,30,31,31,30,31,30,31]

for year in range(1900, 1900+input):
    for month in range(0, 12):
        weekday = (calendarDay+12)%7
        freq[(weekday+2)%7]+=1
        calendarDay += (leapDays[month] if isLeap(year) else normDays[month])

result = ""
for i in range(0, 7):
    result = result + str(freq[i])
    if i == 6:
        result = result + '\n'
    else:
        result = result + ' '

outputFile = open('friday.out', 'w')
outputFile.write(result)
outputFile.close()
