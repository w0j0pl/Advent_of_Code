file = open("input.txt", 'r')

content = file.readlines()
file.close()

res = 0
numbers = []


for i, line in enumerate(content):
    j = 0

    while j < len(line):
        number = []
        while j < len(line) and line[j].isdigit():
            number.append(j)
            j += 1

        if number:
            number.append(i)
            numbers.append(tuple(number))

        j += 1


for num_line, line in enumerate(content):
    for num_ch, ch in enumerate(line):
        if ch == "*":
            multipliers = []

            for array in numbers:
                num = ''

                if array[-1] == num_line - 1:
                    if num_ch - 1 in array[0: -1] or num_ch in array[0: -1] or num_ch + 1 in array[0: -1]:
                        for i in range(len(array) - 1):
                            print(content[num_line - 1][array[i]])
                            num += str(content[num_line - 1][array[i]])
                        multipliers.append(int(num))

                num = ''
                if array[-1] == num_line:
                    if num_ch - 1 in array[0: -1] or num_ch + 1 in array[0: -1]:
                        for i in range(len(array) - 1):
                            print(content[num_line][array[i]])
                            num += str(content[num_line][array[i]])
                        multipliers.append(int(num))

                num = ''
                if array[-1] == num_line + 1:
                    if num_ch - 1 in array[0: -1] or num_ch in array[0: -1] or num_ch + 1 in array[0: -1]:
                        for i in range(len(array) - 1):
                            print(content[num_line + 1][array[i]])
                            num += str(content[num_line + 1][array[i]])
                        multipliers.append(int(num))

            if len(multipliers) == 2:
                res += multipliers[0] * multipliers[1]

print(res)
