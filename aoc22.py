f = open('test_aoc22.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
boss_hp = int(raw_input[0].split(': ')[1])
boss_attack = int(raw_input[1].split(': ')[1])
player_hp = 10
player_mana = 250

played_states = set()
# player_hp, player_mana, player_armor, mana_spent, boss_hp, shield_turns, poison_turns, recharge_turns, next_action)


# next_action: 
# 0: Magic Missile
# 1: Drain
# 2: Shield
# 3: Poison
# 4: Recharge

max_mana_spent = 999999999999999999999
max_actions_taken = []
# Going to do a BFS
# Start by loading each of the initial actions into the action queue

action_queue = []
action_queue += [(player_hp, player_mana, 0, 0, boss_hp, 0,0,0,0,[])]
action_queue += [(player_hp, player_mana, 0, 0, boss_hp, 0,0,0,1,[])]
action_queue += [(player_hp, player_mana, 0, 0, boss_hp, 0,0,0,2,[])]
action_queue += [(player_hp, player_mana, 0, 0, boss_hp, 0,0,0,3,[])]
action_queue += [(player_hp, player_mana, 0, 0, boss_hp, 0,0,0,4,[])]
while action_queue:
    # Player turn
    raw_player_state = action_queue.pop(0)
    player_state = tuple(raw_player_state[:9])
    if player_state in played_states:
        continue
    
    # populate variables
    played_states.add(player_state)
    player_hp = player_state[0]
    player_mana = player_state[1]
    player_armor = player_state[2]
    mana_spent = player_state[3]
    boss_hp = player_state[4]
    shield_turns = player_state[5]
    poison_turns = player_state[6]
    recharge_turns = player_state[7]
    next_action = player_state[8]
    actions_taken = raw_player_state[9][:]

    actions_taken += ['Player turn']
    actions_taken += ['Player has ' + str(player_hp) + ' hit points, ' + str(player_armor) + ' armor, ' + str(player_mana) + ' mana']
    actions_taken += ['Boss has ' + str(boss_hp) + ' hit points']
    # Tick down any effects
    if shield_turns > 0:
        shield_turns -= 1
        actions_taken += ['Shield timer is ' + str(shield_turns)]
    else:
        player_armor = 0
    if poison_turns > 0:
        poison_turns -= 1
        actions_taken += ['Poison damage: 3']
        actions_taken += ['Poison timer is ' + str(poison_turns)]
        boss_hp -= 3
    if recharge_turns > 0:
        recharge_turns -= 1
        player_mana += 101
        actions_taken += ['Recharge provides 101 mana']
        actions_taken += ['Recharge timer is ' + str(recharge_turns)]
    # Check boss health
    if boss_hp <= 0:
        # Boss is dead
        if mana_spent < max_mana_spent:
            max_mana_spent = mana_spent
            max_actions_taken = actions_taken[:]
        continue
    # Apply action
    
    if next_action == 0:
        mana_spent += 53
        player_mana -= 53
        boss_hp -= 4
        actions_taken += ['Magic Missile: Damage 4']
    elif next_action == 1:
        mana_spent += 73
        player_mana -= 73
        boss_hp -= 2
        player_hp += 2
        actions_taken += ['Drain: Damage 2']
    elif next_action == 2:
        mana_spent += 113
        player_mana -= 113
        shield_turns = 6
        player_armor = 7
        actions_taken += ['Shield Cast']
    elif next_action == 3:
        mana_spent += 173
        player_mana -= 173
        poison_turns = 6
        actions_taken += ['Poison Cast']
    elif next_action == 4:
        mana_spent += 229
        player_mana -= 229
        recharge_turns = 5
        actions_taken += ['Recharge Cast']

    if boss_hp <= 0:
        # boss is dead
        if mana_spent < max_mana_spent:
            max_mana_spent = mana_spent
            max_actions_taken = actions_taken[:]
        continue
    # end of player turn, now for boss turn
    actions_taken += ['Boss turn']
    actions_taken += ['Player has ' + str(player_hp) + ' hit points, ' + str(player_armor) + ' armor, ' + str(player_mana) + ' mana']
    actions_taken += ['Boss has ' + str(boss_hp) + ' hit points']
    if shield_turns > 0:
        shield_turns -= 1
        actions_taken += ['Shield timer is ' + str(shield_turns)]
    else:
        player_armor = 0
    if poison_turns > 0:
        poison_turns -= 1
        boss_hp -= 3
        actions_taken += ['Poison damage: 3']
        actions_taken += ['Poison timer is ' + str(poison_turns)]
    if recharge_turns > 0:
        recharge_turns -= 1
        player_mana += 101
        actions_taken += ['Recharge provides 101 mana']
        actions_taken += ['Recharge timer is ' + str(recharge_turns)]
    # Check boss health
    if boss_hp <= 0:
        # Boss is dead
        if mana_spent < max_mana_spent:
            max_mana_spent = mana_spent
            max_actions_taken = actions_taken[:]
        continue
    # Boss attack
    damage = max(1, boss_attack - player_armor)
    player_hp -= damage
    actions_taken += ['Boss attacks for ' + str(damage) + ', player HP is now ' + str(player_hp)]
    if player_hp <= 0:
        # Player is died
        continue
    # Now come up with new options for the next player turn

    # player_hp, player_mana, player_armor, mana_spent, boss_hp, shield_turns, poison_turns, recharge_turns, next_action
    if player_mana < 53:
        continue
    # Magic Missile
    if (player_mana >= 53) or (recharge_turns > 0):
       action_queue += [(player_hp, player_mana, player_armor, mana_spent, boss_hp, shield_turns, poison_turns, recharge_turns, 0, actions_taken)]
    # Drain
    if (player_mana >= 73) or (recharge_turns > 0):
        action_queue += [(player_hp, player_mana, player_armor, mana_spent, boss_hp, shield_turns, poison_turns, recharge_turns, 1, actions_taken)]
    # Shield
    if ((player_mana >= 113) or (recharge_turns > 0)) and (shield_turns == 0):
        action_queue += [(player_hp, player_mana, player_armor, mana_spent, boss_hp, shield_turns, poison_turns, recharge_turns, 2, actions_taken)]
    # Poison
    if ((player_mana >= 173) or (recharge_turns > 0)) and (poison_turns == 0):
        action_queue += [(player_hp, player_mana, player_armor, mana_spent, boss_hp, shield_turns, poison_turns, recharge_turns, 3, actions_taken)]
    # Recharge
    if (player_mana >= 229) and ((recharge_turns == 0) or (recharge_turns == 1)):
        action_queue += [(player_hp, player_mana, player_armor, mana_spent, boss_hp, shield_turns, poison_turns, recharge_turns, 4, actions_taken)]

   
print('Part 1: minimum mana spent is ' + str(max_mana_spent))
print()
# 1362 too high
