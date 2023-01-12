f = open('aoc01.txt','r')
in_data = f.read()
current_floor = 0
current_character = 0
basement = False

for character in in_data:
    current_character += 1
    if character == '(':
        current_floor += 1
    elif character == ')':
        current_floor -= 1
    if current_floor < 0 and basement == False:
        basement = True
        print('Basement entered at character ' + str(current_character))
f.close()
print('Part 1: Ended at ' + str(current_floor))

