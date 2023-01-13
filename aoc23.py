f = open('aoc23.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()

pc = 0
registers = {'a':0, 'b':0}

while (pc < len(raw_input)) and (pc >= 0):
    split_raw_input  = raw_input[pc].replace(',','').split(' ')
   
    
    instruction = split_raw_input[0]
    register = split_raw_input[1]
    # Get the instruction
    if instruction == 'hlf':
        registers[register] //= 2
    elif instruction == 'tpl':
        registers[register] *= 3
    elif instruction == 'inc':
        registers[register] += 1
    elif instruction == 'jmp':
        offset = int(split_raw_input[1]) - 1
        pc += offset
    elif instruction == 'jie':
        if registers[register] % 2 == 0:
            offset = int(split_raw_input[2]) - 1
            pc += offset
        
    elif instruction == 'jio':
        if registers[register] == 1:
            offset = int(split_raw_input[2]) - 1
            pc += offset
    pc += 1
print('Part 1: a is ' + str(registers['a']) + ', b is ' + str(registers['b']))
# b is not 1
registers = {'a':1, 'b':0}
pc = 0
while (pc < len(raw_input)) and (pc >= 0):
    split_raw_input  = raw_input[pc].replace(',','').split(' ')
   
    
    instruction = split_raw_input[0]
    register = split_raw_input[1]
    # Get the instruction
    if instruction == 'hlf':
        registers[register] //= 2
    elif instruction == 'tpl':
        registers[register] *= 3
    elif instruction == 'inc':
        registers[register] += 1
    elif instruction == 'jmp':
        offset = int(split_raw_input[1]) - 1
        pc += offset
    elif instruction == 'jie':
        if registers[register] % 2 == 0:
            offset = int(split_raw_input[2]) - 1
            pc += offset
        
    elif instruction == 'jio':
        if registers[register] == 1:
            offset = int(split_raw_input[2]) - 1
            pc += offset
    pc += 1
print('Part 2: a is ' + str(registers['a']) + ', b is ' + str(registers['b']))
# b is not 1

