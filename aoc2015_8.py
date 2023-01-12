f = open('aoc08.txt','r')
input_text = f.readlines()          
f.close()
code_lengths = 0
string_lengths = 0
for line in input_text:
    my_line = line.strip()
    code_lengths += len(my_line)
    print len(line.strip())
    init_line = line.strip()[1:-1]
    decoded_string = init_line.decode('string_escape')
    string_lengths += len(decoded_string)
print('code lengths: ' + str(code_lengths))
print('String lengths: ' + str(string_lengths))
print('Part 1: ' + str(code_lengths - string_lengths))
# Part 2
encoded_lengths = 0
for line in input_text:
    current_string = line.strip()
    encoded_string = ''
    for character in current_string:
        if character == '"':
            encoded_string += r'\"'
        elif character == '\\':
            encoded_string += '\\\\'
        else:
            encoded_string += character
    encoded_string = '"' + encoded_string + '"'
    #print(len(encoded_string))
    encoded_lengths += len(encoded_string)
print('code lengths: ' + str(code_lengths))
print('encoded lengths: ' + str(encoded_lengths))
print('Part 2: ' + str(encoded_lengths - code_lengths))