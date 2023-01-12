import re
import json

digits = re.compile(r'-?\d+')
f = open('aoc12.txt','r')
input_text = f.readlines()
f.close
rolling_sum = 0
for line in input_text:
    digits_found = digits.findall(line)
    for number in digits_found:
        rolling_sum += int(number)
print('part 1: sum is ' + str(rolling_sum))
parsed = json.loads(input_text[0])
new_sum = 0
def parseList(my_list):
    my_sum = 0
    for item in my_list:
        if isinstance(item, list):
            my_sum += parseList(item)
        elif isinstance(item, dict):
            my_sum += parseDict(item)
        elif item == 'red':
            my_sum += 0
        else:
            digits_found = digits.findall(str(item))
            for number in digits_found:
                my_sum += int(number)  
    return my_sum
            
def parseDict(my_dict):
    my_sum = 0
    for key in my_dict.keys():
        current_item = my_dict[key]
        if isinstance(current_item, list):
            my_sum += parseList(current_item)
        elif isinstance(current_item, dict):
            my_sum += parseDict(current_item)
        elif current_item == 'red':
            return 0
        else:
            digits_found = digits.findall(str(current_item))
            for number in digits_found:
                my_sum += int(number)
    return my_sum
if isinstance(parsed, list):
    new_sum = parseList(parsed)
elif isinstance(parsed, dict):
    new_sum = parseDict(parsed)
    
print('Part 2: ' + str(new_sum))
    
    