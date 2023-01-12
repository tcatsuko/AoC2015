puzzle_input = '1113122113'
current_digit = puzzle_input[0]
digit_count = 0
for loop in xrange(50):
    current_digit = puzzle_input[0]
    digit_count = 0    
    temp_puzzle = []
    for digit in puzzle_input:
        if digit == current_digit:
            digit_count += 1
        else:
            temp_puzzle += [str(digit_count)]
            temp_puzzle += [current_digit]
            current_digit = digit
            digit_count = 1
    if (len(temp_puzzle) == 0) or (temp_puzzle[-1] != digit):
        temp_puzzle += [str(digit_count)]
        temp_puzzle += digit
    puzzle_input = temp_puzzle[:]
    if loop == 39:
        print('part 1: length is ' + str(len(puzzle_input)))
print('Part 2: length is ' + str(len(puzzle_input)))
            