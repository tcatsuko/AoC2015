
f = open('aoc21.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()
weapons = []
armor = []
rings = []

boss_health = int(problem_input[0].split(': ')[1])
boss_attack = int(problem_input[1].split(': ')[1])
boss_armor = int(problem_input[2].split(': ')[1])

print()

weapons = []
weapons += [(8,4,0)]
weapons += [(10,5,0)]
weapons += [(25,6,0)]
weapons += [(40,7,0)]
weapons += [(74,8,0)]
armor = []
armor += [(0,0,0)]
armor += [(13,0,1)]
armor += [(31,0,2)]
armor += [(53,0,3)]
armor += [(75,0,4)]
armor += [(102,0,5)]
rings = []
rings += [(0,0,0)]
rings += [(0,0,0)]
rings += [(25,1,0)]
rings += [(50,2,0)]
rings += [(100,3,0)]
rings += [(20,0,1)]
rings += [(40,0,2)]
rings += [(80,0,3)]

def simulate_game(player, boss):
    player_health = player[0]
    boss_health = boss[0]
    while True:
        player_attack = player[1]
        player_armor = player[2]
        boss_attack = boss[1]
        boss_armor = boss[2]
        player_damage = player_attack - boss_armor
        if player_damage < 1:
            player_damage = 1
        boss_health -= player_damage
        if boss_health <= 0:
            break
        boss_damage = boss_attack - player_armor
        if boss_damage < 1:
            boss_damage = 1
        player_health -= boss_damage
        if player_health <= 0:
            break
    if player_health > 0:
        return True
    else:
        return False

min_cost = 74 + 102 + 100 + 80
max_cost = 0
lowest_combo = (0,0,0,0,0)

for weapon_index in range(len(weapons)):
    current_weapon = weapons[weapon_index]
    
    for armor_index in range(len(armor)):
        current_armor = armor[armor_index]
        for ring1_index in range(len(rings)):
            ring1 = rings[ring1_index]
            for ring2_index in range(ring1_index + 1, len(rings)):
                ring2 = rings[ring2_index]
                player = [100, current_weapon[1] + ring1[1] + ring2[1], current_armor[2] + ring1[2] + ring2[2]]
                boss = [boss_health, boss_attack, boss_armor]
                fight_result = simulate_game(player, boss)
                if fight_result == True:
                    total_cost = current_weapon[0] + current_armor[0] + ring1[0] + ring2[0]
                    if total_cost < min_cost:
                        min_cost = total_cost
                        lowest_combo = (max_cost, weapon_index, armor_index, ring1_index, ring2_index)
                else:
                    total_cost = current_weapon[0] + current_armor[0] + ring1[0] + ring2[0]
                    if total_cost > max_cost:
                        max_cost = total_cost
print('Part 1:')
print('The lowest cost to defeat the boss is ' + str(min_cost))
# 195 too high
# 26 also not right
print('Part 2:')
print('The highest cost spent to lose is ' + str(max_cost))
# 233 too high