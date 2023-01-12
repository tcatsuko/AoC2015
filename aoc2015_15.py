f = open('aoc15.txt','r')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
ingredients = []
for line in raw_input:
    properties = line.split(': ')[1:]
    name = line.split(':')[0]
    ingredient = {}
    ingredient['name'] = name
    for item in properties[0].split(', '):
        ingredient_properties = item.split(', ')
        for new_item in ingredient_properties:
            ingredient[new_item.split(' ')[0]]= int(new_item.split(' ')[1])
    ingredients += [ingredient]
high_score = 0
highest_lowcal = 0
for a in range(101):
    for b in range(101-a):
        for c in range(101-b-a):
            for d in range(101-c-b-a):
                total_capacity = ingredients[0]['capacity'] * a + ingredients[1]['capacity'] * b + ingredients[2]['capacity'] * c + ingredients[3]['capacity'] * d
                if total_capacity < 0:
                    total_capacity = 0
                total_durability = ingredients[0]['durability'] * a + ingredients[1]['durability'] * b + ingredients[2]['durability'] * c + ingredients[3]['durability'] * d
                if total_durability < 0:
                    total_durability = 0
                total_flavor = ingredients[0]['flavor'] * a + ingredients[1]['flavor'] * b + ingredients[2]['flavor'] * c + ingredients[3]['flavor'] * d
                if total_flavor < 0:
                    total_flavor = 0
                total_texture = ingredients[0]['texture'] * a + ingredients[1]['texture'] * b + ingredients[2]['texture'] * c + ingredients[3]['texture'] * d
                if total_texture < 0:
                    total_texture = 0
                total_calories = ingredients[0]['calories'] * a + ingredients[1]['calories'] * b + ingredients[2]['calories'] * c + ingredients[3]['calories'] * d
                score = total_capacity * total_durability * total_flavor * total_texture
                if score > high_score:
                    high_score = score
                    ingredients[0]['amount_highest'] = a
                    ingredients[1]['amount_highest'] = b
                    ingredients[2]['amount_highest'] = c
                    ingredients[3]['amount_highest'] = d
                if total_calories == 500 and score > highest_lowcal:
                    ingredients[0]['amount_lowcal'] = a
                    ingredients[1]['amount_lowcal'] = b
                    ingredients[2]['amount_lowcal'] = c
                    ingredients[3]['amount_lowcal'] = d
                    highest_lowcal = score
                   
print('Part 1:')
print('Total score:' + str(high_score))
print(ingredients[0]['name'] + ': ' + str(ingredients[0]['amount_highest']))
print(ingredients[1]['name'] + ': ' + str(ingredients[1]['amount_highest']))
print(ingredients[2]['name'] + ': ' + str(ingredients[2]['amount_highest']))
print(ingredients[3]['name'] + ': ' + str(ingredients[3]['amount_highest']))
print(' ')
print(' ')
print('Part 2:')
print('Total score: ' + str(highest_lowcal))
print(ingredients[0]['name'] + ': ' + str(ingredients[0]['amount_lowcal']))
print(ingredients[1]['name'] + ': ' + str(ingredients[1]['amount_lowcal']))
print(ingredients[2]['name'] + ': ' + str(ingredients[2]['amount_lowcal']))
print(ingredients[3]['name'] + ': ' + str(ingredients[3]['amount_lowcal']))