file = open("input.txt", 'r')

content = file.readlines()

file.close()

seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

dict = {1: seed_to_soil, 2: soil_to_fertilizer, 3: fertilizer_to_water, 4: water_to_light, 5: light_to_temperature,
        6: temperature_to_humidity, 7: humidity_to_location}

seed = ''

for i in range(len(content[0])):
    if content[0][i].isdigit():
        seed += content[0][i]
    else:
        if len(seed) > 0:
            seeds.append(int(seed))
            seed = ''

digit = False
place = 1
number = ''
for i in range(3, len(content)):
    for j in range(len(content[i])):
        if content[i][j].isdigit():
            number += content[i][j]
            digit = True
        else:
            if len(number) > 0:
                dict[place].append(int(number))
                number = ''
                digit = False

    if digit:
        dict[place].append(int(number))

    if content[i] == '\n':
        place += 1

locations = []

for seed in seeds:
    location = seed

    for key in dict:
        for i in range(1, len(dict[key]), 3):
            if dict[key][i] + dict[key][i + 1] >= location >= dict[key][i]:
                location += dict[key][i - 1] - dict[key][i]
                break

    locations.append(location)

print(min(locations))

