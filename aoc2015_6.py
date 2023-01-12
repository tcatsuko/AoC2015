import re
digitsRegex = re.compile(r'\D*(\d*\d*\d),(\d*\d*\d)\D*(\d*\d*\d),(\d*\d*\d)')
f = open('aoc06.txt','r')
input_test = f.readlines()
f.close
lightArray = []
for y in xrange(1000):
    currentRow = []
    for x in xrange(1000):
        currentRow += [0]
    lightArray += [currentRow]
for line in input_test:
    found_coordinates = digitsRegex.findall(line)[0]
    xStart = int(found_coordinates[0])
    xEnd = int(found_coordinates[2]) + 1
    yStart = int(found_coordinates[1])
    yEnd = int(found_coordinates[3]) + 1
    turnOn = 'turn on' in line
    turnOff = 'turn off' in line
    toggle = 'toggle' in line
    for y in xrange(yStart, yEnd):
        for x in xrange(xStart, xEnd):
            if turnOn:
                lightArray[y][x] = 1
            elif turnOff:
                lightArray[y][x] = 0
            elif toggle:
                if lightArray[y][x] == 0:
                    lightArray[y][x] = 1
                else:
                    lightArray[y][x] = 0
part1_sum = 0
for row in lightArray:
    part1_sum += sum(row)
print('Part 1: there are ' + str(part1_sum) + ' lights on.')
lightArray = []
for y in xrange(1000):
    currentRow = []
    for x in xrange(1000):
        currentRow += [0]
    lightArray += [currentRow]
for line in input_test:
    found_coordinates = digitsRegex.findall(line)[0]
    xStart = int(found_coordinates[0])
    xEnd = int(found_coordinates[2]) + 1
    yStart = int(found_coordinates[1])
    yEnd = int(found_coordinates[3]) + 1
    turnOn = 'turn on' in line
    turnOff = 'turn off' in line
    toggle = 'toggle' in line
    for y in xrange(yStart, yEnd):
        for x in xrange(xStart, xEnd):
            if turnOn:
                lightArray[y][x] += 1
            elif turnOff:
                if lightArray[y][x] == 0:   
                    lightArray[y][x] = 0
                else:
                    lightArray[y][x] -= 1
            elif toggle:
                lightArray[y][x] += 2
part2_sum = 0
for row in lightArray:
    part2_sum += sum(row)
print('Part 2: there are ' + str(part2_sum) + ' lights on.')