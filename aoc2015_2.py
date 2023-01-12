f = open('aoc02.txt','r')
input_text = f.readlines()
f.close()
total_area = 0
smallest_area = 0
smallest_perim = 0
ribbon = 0

for line in input_text:
    line.strip()
    (l,w,h) = line.split('x')
    area1 = int(l) * int(w)
    area2 = int(w) * int(h)
    area3 = int(l) * int(h)
    perim1 = (2 * int(l)) + (2 * int(w))
    perim2 = (2 * int(w)) + (2 * int(h))
    perim3 = (2 * int(l)) + (2 * int(h))
    cubic = int(w) * int(l) * int(h)
    smallest_perim = perim1
    if perim2 < smallest_perim:
        smallest_perim = perim2
    if perim3 < smallest_perim:
        smallest_perim = perim3
    current_ribbon = cubic + smallest_perim
    ribbon += current_ribbon
    current_area = (2*area1)+(2*area2)+(2*area3)
    smallest_area = area1
    if area2 < smallest_area:
        smallest_area = area2
    if area3 < smallest_area:
        smallest_area = area3
    current_area += smallest_area
    total_area += current_area
print('part 1: ' + str(total_area))
print('part 2: ' + str(ribbon))


    
    
