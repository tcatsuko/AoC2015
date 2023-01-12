import hashlib
key = 'bgvyzdsv'
number = 0
found_hash = False
while not found_hash:
    test_number = key + str(number)
    result = hashlib.md5(test_number.encode())
    if result.hexdigest()[0:5] == '00000':
        found_hash = True
    else:
        number += 1
print('part 1: ' + str(number))
number = 0
found_hash = False
while not found_hash:
    test_number = key + str(number)
    result = hashlib.md5(test_number.encode())
    if result.hexdigest()[0:6] == '000000':
        found_hash = True
    else:
        number += 1
print('part 2: ' + str(number))

        
    