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

dict = {0: seed_to_soil, 1: soil_to_fertilizer, 2: fertilizer_to_water, 3: water_to_light, 4: light_to_temperature,
        5: temperature_to_humidity, 6: humidity_to_location}

num_count = 0
number = ''
numbers = []
for i in range(len(content[0])):
    if content[0][i].isdigit():
        number += content[0][i]
    else:
        num_count += 1
        if len(number) > 0:
            if num_count % 2 == 0:
                numbers.append(int(number))
            else:
                numbers.append(int(number) + numbers[-1] - 1)
                seeds.append(numbers)
                numbers = []
        number = ''

digit = False
numbers = []
number = ''
place = 0
for i in range(3, len(content)):
    for j in range(len(content[i])):
        if content[i][j].isdigit():
            number += content[i][j]
            digit = True
        else:
            if len(number) > 0:
                numbers.append(int(number))
                number = ''
                digit = False
        if len(numbers) == 3:
            dict[place].append(numbers)
            numbers = []
    if digit:
        numbers.append(int(number))
        dict[place].append(numbers)
    if content[i] == '\n':
        place += 1

for i in range(len(dict)):
    dict[i] = sorted(dict[i], key=lambda x: x[1])

stage0 = []
stage1 = []
stage2 = []
stage3 = []
stage4 = []
stage5 = []
stage6 = []

stages = {0: stage0, 1: stage1, 2: stage2, 3: stage3, 4: stage4, 5: stage5, 6: stage6}

for stage in range(len(stages)):
    for i in range(len(dict[stage])):
        stages[stage].append([dict[stage][i][0] - dict[stage][i][1], dict[stage][i][1], dict[stage][i][1] + dict[stage][i][2] - 1])
    stages[stage] = sorted(stages[stage], key=lambda x: x[1])
    print(stages[stage])

stage0_seeds = []
stage1_seeds = []
stage2_seeds = []
stage3_seeds = []
stage4_seeds = []
stage5_seeds = []
stage6_seeds = []
stage7_seeds = []

stages_seeds = {0: stage0_seeds, 1: stage1_seeds, 2: stage2_seeds, 3: stage3_seeds, 4: stage4_seeds, 5: stage5_seeds, 6: stage6_seeds, 7: stage7_seeds}

for seed in seeds:
    for i in range(len(stages[0])):
        if stages[0][i][2] >= seed[0] >= stages[0][i][1]:
            if stages[0][i][2] >= seed[1] >= stages[0][i][1]:
                stages_seeds[0].append([seed[0] + stages[0][i][0], seed[1] + stages[0][i][0]])
                seed = [-1, -1]
                break
            else:
                stages_seeds[0].append([seed[0] + stages[0][i][0], stages[0][i][0] + stages[0][i][2]])
                seed[0] = stages[0][i][2] + 1

        elif stages[0][i][2] >= seed[1] >= stages[0][i][1]:
            stages_seeds[0].append([stages[0][i][0] + stages[0][i][1], seed[1] + stages[0][i][0]])
            seed[1] = stages[0][i][1] - 1
    if seed != [-1, -1]:
        stages_seeds[0].append([seed[0], seed[1]])
    print(stages_seeds[0], 0)


for stage_seed in range(6):
    for seed in stages_seeds[stage_seed]:
        # print(stages_seeds[stage_seed])
        for i in range(len(stages[stage_seed + 1])):
            if stages[stage_seed + 1][i][2] >= seed[0] >= stages[stage_seed + 1][i][1]:
                if stages[stage_seed + 1][i][2] >= seed[1] >= stages[stage_seed + 1][i][1]:
                    stages_seeds[stage_seed + 1].append([seed[0] + stages[stage_seed + 1][i][0], seed[1] + stages[stage_seed + 1][i][0]])
                    seed = [-1, -1]
                    break
                else:
                    stages_seeds[stage_seed + 1].append([seed[0] + stages[stage_seed + 1][i][0], stages[stage_seed + 1][i][0] + stages[stage_seed + 1][i][2]])
                    seed[0] = stages[stage_seed + 1][i][2] + 1

            elif stages[stage_seed + 1][i][2] >= seed[1] >= stages[stage_seed + 1][i][1]:
                stages_seeds[stage_seed + 1].append([stages[stage_seed + 1][i][0] + stages[stage_seed + 1][i][1], seed[1] + stages[stage_seed + 1][i][0]])
                seed[1] = stages[stage_seed + 1][i][1] - 1

        if seed != [-1, -1]:
            stages_seeds[stage_seed + 1].append([seed[0], seed[1]])
        print(stages_seeds[stage_seed + 1], stage_seed + 1)


stage6_seeds = sorted(stage6_seeds, key=lambda x: x[0])
print(stage6_seeds)
