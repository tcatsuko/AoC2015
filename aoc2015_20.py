from functools import reduce
import numpy as np

def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

target = 29000000
#target = 150
for x in range(1, target / 10):
    sum = 0
    for item in factors(x):
        sum += 10 * item
    if sum >= target:
        break
print('Part 1:')
print('The lowest house number to get at least ' + str(target) + ' presents is ' + str(x))

# max number - we will try to double things

for x in range(1, target / 10):
    
    sum = 0
    if x % 10000 == 0:
        print(x)
    for item in factors(x):
        if (x / item) <= 50:
            sum += 11 * item
        else:
            sum += 11 * 50
            
    if sum >= target:
        break
print('Part 2:')
print('The lowest house number to get at least ' + str(target) + ' presents is ' + str(x))
# 811080 too high
# 718200 too high
