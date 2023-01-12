f = open('aoc07.txt','r')
input_text = f.readlines()
f.close()
final_values = {}
values_to_calculate = {}
for line in input_text:
    stripped = line.strip()
    split_instructions = stripped.split(' -> ')
    if split_instructions[1] == 'a':
        print()
    try:
        intValue = int(split_instructions[0])
        final_values[split_instructions[1]] = intValue
    except ValueError:
        values_to_calculate[split_instructions[1]] = split_instructions[0]
# Main loop
final_values2 = final_values.copy()
def calc_value(wire):
    if wire in final_values:
        return
    if wire == 'a':
        print()
    operation = values_to_calculate[wire]
    # Determine operation
    split_op = operation.split(' ')
    if 'AND' in split_op:
        op1 = split_op[0]
        op2 = split_op[2]
        opval1 = -1
        opval2 = -1
        try:
            opval1 = int(op1)
        except ValueError:
            if op1 in final_values:
                opval1 = final_values[op1]
            else:
                opval1 = calc_value(op1)
        try:
            opval2 = int(op2)
        except ValueError:
            if op2 in final_values:
                opval2 = final_values[op2]
            else:
                opval2 = calc_value(op2)
        result = opval1 & opval2
    elif 'LSHIFT' in split_op:
        op1 = split_op[0]
        opval1 = -1
        opval2 = int(split_op[2])
        try:
            opval1 = int(op1)
        except ValueError:
            if op1 in final_values:
                opval1 = final_values[op1]
            else:
                opval1 = calc_value(op1)
        result = opval1 << opval2
    elif 'NOT' in split_op:
        op1 = split_op[1]
        opval1 = -1
        try:
            opval1 = int(op1)
        except ValueError:
            if op1 in final_values:
                opval1 = final_values[op1]
            else:
                opval1 = calc_value(op1)
        result = ~opval1
    elif 'OR' in split_op:
        op1 = split_op[0]
        op2 = split_op[2]
        opval1 = -1
        opval2 = -1
        try:
            opval1 = int(op1)
        except ValueError:
            if op1 in final_values:
                opval1 = final_values[op1]
            else:
                opval1 = calc_value(op1)
        try:
            opval2 = int(op2)
        except ValueError:
            if op2 in final_values:
                opval2 = final_values[op2]
            else:
                opval2 = calc_value(op2)
        result = opval1 | opval2  
    elif 'RSHIFT' in split_op:
        op1 = split_op[0]
        opval1 = -1
        opval2 = int(split_op[2])
        try:
            opval1 = int(op1)
        except ValueError:
            if op1 in final_values:
                opval1 = final_values[op1]
            else:
                opval1 = calc_value(op1)
        result = opval1 >> opval2
    else:
        # Direct assignment
        op1 = split_op[0]
        opval1 = -1
        try:
            opval1 = int(op1)
        except ValueError:
            if op1 in final_values:
                opval1 = final_values[op1]
            else:
                opval1 = calc_value(op1)
        result = opval1
    if result < 0:
        result = result & 0xFFFF
    final_values[wire] = result
    return result
for key in values_to_calculate.keys():
    result = calc_value(key)
for key in final_values:
    print(key + ': ' + str(final_values[key]))
print('Part 1: the value of a is ' + str(final_values['a']))
override_b = final_values['a']
final_values = final_values2
final_values['b'] = override_b
for key in values_to_calculate.keys():
    result = calc_value(key)
print('Part 2: the value of a is ' + str(final_values['a']))
