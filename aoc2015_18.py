f = open('aoc18.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()
print()
def listifyString(string):
    myList = []
    myList[:0] = string
    return myList
game_array = []
for line in problem_input:
    game_array += [listifyString(line)]
rows = len(game_array)
columns = len(game_array[0])
steps = 100
for step in range(steps):
    new_game_array = []
    for row in range(rows):
        new_row = []
        for column in range(columns):
            # Check neighbors, clockwise, starting from top
            on_neighbors = 0
            if (row >  0) and (game_array[row-1][column] == '#'):
                on_neighbors += 1
            if (row > 0) and (column <= columns - 2) and (game_array[row-1][column + 1] == '#'):
                on_neighbors += 1
            if (column <= columns - 2) and (game_array[row][column + 1] == '#'):
                on_neighbors += 1
            if (column <= columns - 2) and (row <= rows - 2) and (game_array[row + 1][column + 1] == '#'):
                on_neighbors += 1
            if (row <= rows - 2) and (game_array[row+1][column] == '#'):
                on_neighbors += 1
            if (row <= rows - 2) and (column > 0) and (game_array[row + 1][column - 1] == '#'):
                on_neighbors += 1
            if (column > 0) and (game_array[row][column - 1] == '#'):
                on_neighbors += 1
            if (row > 0) and (column > 0) and (game_array[row - 1][column - 1] == '#'):
                on_neighbors += 1
            if game_array[row][column] == '#':
                if (on_neighbors == 2) or (on_neighbors == 3):
                    new_row += '#'
                else:
                    new_row += '.'
            else:
                if on_neighbors == 3:
                    new_row += '#'
                else:
                    new_row += '.'
        new_game_array += [new_row]
    game_array = new_game_array

on_count = 0
for row in game_array:
    on_count += row.count('#')
print('Part 1:')
print('There are ' + str(on_count) + ' lights on')

game_array = []
for line in problem_input:
    game_array += [listifyString(line)]
rows = len(game_array)
columns = len(game_array[0])
steps = 100
game_array[0][0] = '#'
game_array[0][columns - 1] = '#'
game_array[rows - 1][0] = '#'
game_array[rows - 1][columns - 1] = '#'

for step in range(steps):
    new_game_array = []
    for row in range(rows):
        new_row = []
        for column in range(columns):
            # Check neighbors, clockwise, starting from top
            on_neighbors = 0
            if (row >  0) and (game_array[row-1][column] == '#'):
                on_neighbors += 1
            if (row > 0) and (column <= columns - 2) and (game_array[row-1][column + 1] == '#'):
                on_neighbors += 1
            if (column <= columns - 2) and (game_array[row][column + 1] == '#'):
                on_neighbors += 1
            if (column <= columns - 2) and (row <= rows - 2) and (game_array[row + 1][column + 1] == '#'):
                on_neighbors += 1
            if (row <= rows - 2) and (game_array[row+1][column] == '#'):
                on_neighbors += 1
            if (row <= rows - 2) and (column > 0) and (game_array[row + 1][column - 1] == '#'):
                on_neighbors += 1
            if (column > 0) and (game_array[row][column - 1] == '#'):
                on_neighbors += 1
            if (row > 0) and (column > 0) and (game_array[row - 1][column - 1] == '#'):
                on_neighbors += 1
            if game_array[row][column] == '#':
                if (on_neighbors == 2) or (on_neighbors == 3):
                    new_row += '#'
                else:
                    new_row += '.'
            else:
                if on_neighbors == 3:
                    new_row += '#'
                else:
                    new_row += '.'
        new_game_array += [new_row]
    game_array = new_game_array
    game_array[0][0] = '#'
    game_array[0][columns - 1] = '#'
    game_array[rows - 1][0] = '#'
    game_array[rows - 1][columns - 1] = '#'
    
on_count = 0
for row in game_array:
    on_count += row.count('#')
print('Part 2:')
print('There are ' + str(on_count) + ' lights on')