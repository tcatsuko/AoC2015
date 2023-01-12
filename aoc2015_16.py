f = open('aoc16.txt','r')
raw_input = []
for line in f:
    raw_input += [line[4:-1]]
f.close()
sue_number = 1
aunts = []
for line in raw_input:
    current_sue = {}
    if sue_number < 10:
        stripped_line = line[3:]
    elif sue_number >= 10 and sue_number < 100:
        stripped_line = line[4:]
    else:
        stripped_line = line[5:]
    split_line = stripped_line.split(', ')
    for item in split_line:
        data = item.split(': ')
        current_sue['number'] = sue_number
        current_sue[data[0]] = int(data[1])
    aunts += [current_sue]
    sue_number += 1
possible_aunts = []
target_aunt = {}
target_aunt['children'] = 3
target_aunt['cats'] = 7
target_aunt['samoyeds'] = 2
target_aunt['pomeranians'] = 3
target_aunt['akitas'] = 0
target_aunt['vizslas'] = 0
target_aunt['goldfish'] = 5
target_aunt['trees'] = 3
target_aunt['cars'] = 2
target_aunt['perfumes'] = 1

for aunt in aunts:
    matches = 0
    properties = len(aunt.keys()) - 1
    
    for key in aunt.keys():
        if key == 'number':
            continue
        if aunt[key] == target_aunt[key]:
            matches += 1
    if matches == properties:
        possible_aunts += [aunt]
print('Part 1: aunt number ' + str(possible_aunts[0]['number']) + ' gave you the present')

possible_aunts = []
for aunt in aunts:
    matches = 0
    properties = len(aunt.keys()) - 1
    
    for key in aunt.keys():
        if key == 'number':
            continue
        if key == 'cats':
            if aunt['cats'] > target_aunt['cats']:
                matches += 1
        elif key == 'trees':
            if aunt['trees'] > target_aunt['trees']:
                matches += 1
        elif key == 'pomeranians':
            if aunt['pomeranians'] < target_aunt['pomeranians']:
                matches += 1
        elif key == 'goldfish':
            if aunt['goldfish'] < target_aunt['goldfish']:
                matches += 1
        else:
            if aunt[key] == target_aunt[key]:
                matches += 1
    if matches == properties:
        possible_aunts += [aunt]
print('Part 2: aunt number ' + str(possible_aunts[0]['number']) + ' gave you the present')   
