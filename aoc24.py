from functools import reduce
from itertools import combinations
from operator import mul

f = open('aoc24.txt.','rt')
raw_input = []
for line in f:
    raw_input += [int(line[:-1])]
f.close()
# Get the weight of each portion of the sleigh
section_weight = sum(raw_input) // 3
possible_values = set()
# Get the possible combinations
raw_input.reverse()
def get_qe(splits):
    global raw_input
    group_weight = sum(raw_input) // splits
    for packages in range(len(raw_input)):
        qe = [reduce(mul, x) for x in combinations(raw_input, packages) if sum(x) == group_weight]
        if qe:
            return min(qe)

qe = get_qe(3)
print('part 1: minimum QE is ' + str(qe))
qe = get_qe(4)
print('part 2: minimum QE is ' + str(qe))
