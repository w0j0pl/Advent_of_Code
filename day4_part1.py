file = open('input.txt', 'r')

content = file.readlines()

file.close()

res = 0
my_numbers = []
winning_numbers = []

for i, line in enumerate(content):
    my_number = []
    winning_number = []
    j = 0
    separator = False

    while j < len(line):
        number = ''
        while j < len(line) and line[j].isdigit():
            number += line[j]
            j += 1

        if not separator and line[j] == '|':
            separator = True

        if len(number) > 0:
            if not separator:
                my_number.append(number)
            else:
                winning_number.append(number)
        j += 1

    my_number.append(1)
    my_numbers.append(my_number)
    winning_numbers.append(winning_number)

for i in range(len(my_numbers)):
    count = 0
    for j in range(1, len(my_numbers[i]) - 1):
        if my_numbers[i][j] in winning_numbers[i]:
            count += 1

    res += my_numbers[i][-1]

    for k in range(1, count + 1):
        my_numbers[i + k][-1] += my_numbers[i][-1]
        print(i+k, my_numbers[i + k][-1])

print(res)
