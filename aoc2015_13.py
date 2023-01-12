from itertools import permutations

f = open('aoc13.txt','r')
input_text = f.readlines()
f.close()
# Parse into dictionaries
people = {}
names = []

for line in input_text:
    line_items = line.strip().split(' ')
    first_person = line_items[0]
    if line_items[2] == 'gain':
        multiplier = 1
    else:
        multiplier = -1
    second_person = line_items[10][:-1]
    units = int(line_items[3]) * multiplier
    if first_person not in names:
        names += [first_person]
    if second_person not in names:
        names += [second_person]
    if first_person not in people:
        people[first_person] = {}
    people[first_person][second_person] = units
    people[first_person]['happiness'] = 0
        
permutation_input = names[1:]

def total_happiness():
    total = 0
    for key in people.keys():
        total += people[key]['happiness']
    return total

def reset_happiness():
    for key in people.keys():
        people[key]['happiness'] = 0

perm = permutations(names[1:])
happiness = 0
for i in list(perm):
    reset_happiness()
    # determine first pair happiness and last pair happiness
    people[names[0]]['happiness'] += people[names[0]][i[0]]
    people[i[0]]['happiness'] += people[i[0]][names[0]]
    people[names[0]]['happiness'] += people[names[0]][i[-1]]
    people[i[-1]]['happiness'] += people[i[-1]][names[0]]
    for j in xrange(len(i) - 1):
        people[i[j]]['happiness'] += people[i[j]][i[j+1]]
        people[i[j+1]]['happiness'] += people[i[j+1]][i[j]]
    this_happiness = total_happiness()
    if this_happiness > happiness:
        happiness = this_happiness
print('part 1: total happiness is ' + str(happiness))
# Part 2
people['Brox'] = {}
people['Brox']['happiness'] = 0

for key in people.keys():
    if key == 'Brox':
        continue
    people[key]['Brox'] = 0
    people['Brox'][key] = 0
names += ['Brox']

perm = permutations(names[1:])
happiness = 0
for i in list(perm):
    reset_happiness()
    # determine first pair happiness and last pair happiness
    people[names[0]]['happiness'] += people[names[0]][i[0]]
    people[i[0]]['happiness'] += people[i[0]][names[0]]
    people[names[0]]['happiness'] += people[names[0]][i[-1]]
    people[i[-1]]['happiness'] += people[i[-1]][names[0]]
    for j in xrange(len(i) - 1):
        people[i[j]]['happiness'] += people[i[j]][i[j+1]]
        people[i[j+1]]['happiness'] += people[i[j+1]][i[j]]
    this_happiness = total_happiness()
    if this_happiness > happiness:
        happiness = this_happiness
print('part 2: total happiness is ' + str(happiness))