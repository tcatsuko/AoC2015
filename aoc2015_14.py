f = open('aoc14.txt','r')
input_text = f.readlines()
f.close()

# Parse out the text
reindeer = {}
for line in input_text:
    line_parts = line.strip().split(' ')
    name = line_parts[0]
    speed = int(line_parts[3])
    fly_time = int(line_parts[6])
    rest_time = int(line_parts[13])
    reindeer[name] = {}
    reindeer[name]['flying'] = True
    reindeer[name]['fly_time'] = fly_time
    reindeer[name]['rest_time'] = rest_time
    reindeer[name]['speed'] = speed
    reindeer[name]['distance'] = 0
    reindeer[name]['timer'] = fly_time
    reindeer[name]['points'] = 0

# Now run the sim
for i in xrange(2503):
    for name in reindeer.keys():
        if reindeer[name]['flying'] == True:
            reindeer[name]['distance'] += reindeer[name]['speed']
        reindeer[name]['timer'] -= 1
        if reindeer[name]['timer'] == 0:
            if reindeer[name]['flying'] == True:
                reindeer[name]['flying'] = False
                reindeer[name]['timer'] = reindeer[name]['rest_time']
            else:
                reindeer[name]['flying'] = True
                reindeer[name]['timer'] = reindeer[name]['fly_time']
        winning_distance = 0
    for name in reindeer.keys():
        if reindeer[name]['distance'] > winning_distance:
            winning_distance = reindeer[name]['distance']
    for name in reindeer.keys():
        if reindeer[name]['distance'] == winning_distance:
            reindeer[name]['points'] += 1

# determine winner
winning_distance = 0
winning_points = 0
for name in reindeer.keys():
    if reindeer[name]['distance'] > winning_distance:
        winning_distance = reindeer[name]['distance']
    if reindeer[name]['points'] > winning_points:
        winning_points = reindeer[name]['points']
print('Part 1: winning distance is ' + str(winning_distance))
print('Part 2: winning points is ' + str(winning_points))