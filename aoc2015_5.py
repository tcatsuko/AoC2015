import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
repeatRegex = re.compile(r'(.)\1{1}')
bad1 = re.compile(r'(ab)+')
bad2 = re.compile(r'(cd)+')
bad3 = re.compile(r'(pq)+')
bad4 = re.compile(r'(xy)+')

f = open('aoc05.txt','r')
input_lines = f.readlines()
f.close()
naughty = []
nice = []

for line in input_lines:
    my_line = line.strip()
    vowelResult = len(vowelRegex.findall(my_line))
    repeatResult = len(repeatRegex.findall(my_line))
    badResult1 = len(bad1.findall(my_line))
    badResult2 = len(bad2.findall(my_line))
    badResult3 = len(bad3.findall(my_line))
    badResult4 = len(bad4.findall(my_line))
    
    if (vowelResult >= 3) and (repeatResult >= 1) and (badResult1 == 0) and (badResult2 == 0) and (badResult3 == 0) and (badResult4 == 0):
        nice += [my_line]
    else:
        naughty += [my_line]
print('Nice: ' + str(len(nice)))
print(nice)
print('Naughty: ' + str(len(naughty)))
print(naughty)

# Part 2
nice = []
naughty = []
repeatGroup = re.compile(r'(\w{2})\w*\1')
repeatLetter = re.compile(r'(\w)\w\1')
for line in input_lines:
    my_line = line.strip()
    groupCount = repeatGroup.findall(my_line)
    letterCount = repeatLetter.findall(my_line)
    if (len(groupCount) > 0) and (len(letterCount) > 0):
        nice += [my_line]
    else:
        naughty += [my_line]
print('Part 2:')
print('nice: ' + str(len(nice)))
print('naughty: ' + str(len(naughty)))
