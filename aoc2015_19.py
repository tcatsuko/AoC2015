import re
filename = 'aoc19.txt'
f = open('aoc19.txt','r')
problem_input = []
for line in f:
    problem_input += [line]
f.close()

rules = []
rules_dict = {}
for x in range(len(problem_input)):
    if problem_input[x] == '\n':
        break
    rule = problem_input[x].split(' => ')
    rules += [rule]
    target = rule[0]
    sub = rule[1][:-1]
    if target not in rules_dict:
        rules_dict[target] = []
        rules_dict[target] += [sub]
    else:
        rules_dict[target] += [sub]
initial_molecule = problem_input[-1]
molecules = set()
for rule in rules:
    target = rule[0]
    sub = rule[1][:-1]
    found_targets = [m.start() for m in re.finditer(target, initial_molecule)]
    for index in found_targets:
        earlier_molecule = initial_molecule[0:index]
        later_molecule = initial_molecule[index+len(target):]
        new_molecule = earlier_molecule + sub + later_molecule
        molecules.add(new_molecule)
print('Part 1:')
print(str(len(molecules)) + ' distinct molecules can be created')

f = open('aoc19.txt','r')
problem_input = f.read()
f.close()
molecule = problem_input.split('\n')[-2][::-1]
split_input = problem_input.split('\n')
molecule = split_input[-1][::-1]
reps = {m[1][::-1]: m[0][::-1] for m in re.findall(r'(\w+) => (\w+)', problem_input)}
def rep(x):
    return reps[x.group()]

count = 0
while molecule != 'e':
    molecule = re.sub('|'.join(reps.keys()), rep, molecule, 1)
    count += 1

print('Part 2:')
print('It takes ' + str(count) + ' steps to synthesize this molecule.')
