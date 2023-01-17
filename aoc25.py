f = open('aoc25.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()

#To continue, please consult the code grid in the manual.  Enter the code at row 2981, column 3075.
location = raw_input[0].split('row ')[1].replace(',','').split(' ')
target_row = int(location[0])
target_col = int(location[2][:-1])
max_size = max([target_row, target_col])
print()
number_grid = [[20151125]]
previous_number = 20151125
for max_row in range(1,(max_size + 1) * 2):
# for max_row in range(1, 7):
    number_grid += [[]]
    row = max_row
    for column in range(max_row + 1):
        new_number = (previous_number * 252533) % 33554393
        number_grid[row] += [new_number]
        previous_number = new_number
        row -= 1
relevant_number = number_grid[target_row - 1][target_col - 1]
print('Part 1: The code is ' + str(relevant_number))
