f = open('aoc03.txt','r')
input_text = f.readlines()
f.close()
x = 0
y = 0
houses={}
houses[(0,0)] =1
for character in input_text[0]:
    if character == '<':
        x -= 1
    elif character == '>':
        x += 1
    elif character == '^':
        y += 1
    elif character == 'v':
        y -= 1
    if (x,y) in houses:
        houses[(x,y)] += 1
    else:
        houses[(x,y)] = 1
print('part 1: ' + str(len(houses)))
s_x = 0
s_y = 0
r_x = 0
r_y = 0
santa = True
part2_houses = {}
part2_houses[(0,0)] = 1
for character in input_text[0]:
    if santa:
        x = s_x
        y = s_y
    else:
        x = r_x
        y = r_y
    if character == '<':
        x -= 1
    elif character == '>':
        x += 1
    elif character == '^':
        y += 1
    elif character == 'v':
        y -= 1
    if (x,y) in part2_houses:
        part2_houses[(x,y)] += 1
    else:
        part2_houses[(x,y)] = 1
    if santa:
        s_x = x
        s_y = y
    else:
        r_x = x
        r_y = y
    santa = not santa
print('part 2: ' + str(len(part2_houses)))
        
        
        