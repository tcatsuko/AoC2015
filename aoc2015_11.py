import re
current_password = 'cqjxjnds'
def rule_one(password):
    # Doing this the hard way
    if 'abc' in password:
        return True
    elif 'bcd' in password:
        return True
    elif 'cde' in password:
        return True
    elif 'def' in password:
        return True
    elif 'efg' in password:
        return True
    elif 'fgh' in password:
        return True    
    elif 'ghj' in password:
        return True
    elif 'hjk' in password:
        return True
    elif 'jkm' in password:
        return True
    elif 'kmn' in password:
        return True
    elif 'mnp' in password:
        return True
    elif 'npq' in password:
        return True
    elif 'pqr' in password:
        return True
    elif 'qrs' in password:
        return True
    elif 'rst' in password:
        return True
    elif 'stu' in password:
        return True
    elif 'tuv' in password:
        return True
    elif 'uvw' in password:
        return True
    elif 'vwx' in password:
        return True
    elif 'wxy' in password:
        return True
    elif 'xyz' in password:
        return True   
    else:
        return False
def rule_two(password):
    if 'i' in password:
        return False
    elif 'o' in password:
        return False
    elif 'l' in password:
        return False
    else:
        return True
def rule_three(password):
    initial_character = password[0]
    repeat_groups = 0
    repeat = 0
    found_characters = {}
    for character in xrange(7):
        compare_character = password[character + 1]
        if compare_character == initial_character:
            if compare_character in found_characters:
                found_characters[compare_character] += 1
            else:
                found_characters[compare_character] = 2
        initial_character = compare_character
    # Now to check
    if len(found_characters) >= 2:
        # Possibly passes
        for key in found_characters.keys():
            if found_characters[key] % 2 == 1:
                return False
    else:
        return False
    return True
def check_rules(password):
    if rule_one(password) == False:
        return False
    if rule_two(password) == False:
        return False
    if rule_three(password) == False:
        return False
    return True
def iter_password(password, position):
    old_password = list(password)
    old_password[position] = chr(((ord(old_password[position])+1)%97)%26+97)
    new_password = ''.join([str(x) for x in old_password])
    if ord(new_password[position]) == 97:
        next_position = position - 1
        if next_position < 0:
            next_position = 7
        new_password = iter_password(new_password, next_position)
    return new_password

while check_rules(current_password) == False:
    current_password = iter_password(current_password,7)
print('Part 1: next good password is ' + str(current_password))
current_password = iter_password(current_password, 7)
while check_rules(current_password) == False:
    current_password = iter_password(current_password,7)
print('Part 2: next good password is ' + str(current_password))



    
    
    