f = open('aoc17.txt','r')
problem_input = []
for line in f:
    problem_input += [int(line[:-1])]
f.close()
target_sum = 150
solutions = set()
solution_count = 0
minimum_containers = 99999999999999999999
minimum_count = 0
problem_input.sort(reverse = True)
def find_addends(target_sum, initial_value, remaining_values, containers_used):
    global minimum_containers
    global minimum_count
    
    remainder = target_sum - initial_value
    solution_count = 0
    temp_array = []
    for item in remaining_values:
        if item < remainder:
            temp_array += [item]
        elif item == remainder:
            current_containers_used = containers_used + 1
            if current_containers_used < minimum_containers:
                minimum_containers = current_containers_used
                minimum_count = 1
            elif current_containers_used == minimum_containers:
                minimum_count += 1
            solution_count += 1
    remaining_values = temp_array
    for x in range(len(remaining_values)):
        new_value = initial_value + remaining_values[x]
        solution_count += find_addends(target_sum, new_value, remaining_values[x+1:], containers_used + 1)
    return solution_count
for x in range(len(problem_input) - 1):
    initial_value = problem_input[x]
    remaining_values = problem_input[x+1:]
    
    solution_count += find_addends(target_sum, initial_value, remaining_values, 1)
print('Part 1:')
print('There are ' + str(solution_count) + ' possible combinations')

print('Part 2:')
print('There are ' + str(minimum_count) + ' ways to use minimum containers')

