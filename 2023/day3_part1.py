file = open("input.txt", 'r')

res = 0
correct = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
collection = set(correct)

content = file.readlines()
file.close()


def check(line, start, end):
    for i in range(start, end + 1):
        if i < len(content[line]) - 2 and i > -1 and content[line][i] not in collection:
            return True
    return False


for i, line in enumerate(content):
    j = 0

    while j < len(line) - 1:
        indexes = []
        while line[j].isdigit() and j < len(line) - 1:
            indexes.append(j)
            j += 1

        if len(indexes) > 0:
            print(len(line), indexes[0], indexes[-1])
            if i == 0:
                if indexes[0] == 0:
                    if (line[indexes[-1] + 1] not in collection or
                       check(i + 1, indexes[0] - 1, indexes[-1] + 1)):

                        number = ''

                        for idx in indexes:
                            number += line[idx]

                        res += int(number)

                elif indexes[-1] == len(line) - 2:
                    if (line[indexes[0] - 1] not in collection or
                       check(i + 1, indexes[0] - 1, indexes[-1] + 1)):

                        number = ''

                        for idx in indexes:
                            number += line[idx]

                        res += int(number)

                else:
                    if (line[indexes[-1] + 1] not in collection or
                       line[indexes[0] - 1] not in collection or
                       check(i + 1, indexes[0] - 1, indexes[-1] + 1)):

                        number = ''

                        for idx in indexes:
                            number += line[idx]

                        res += int(number)

            elif i == len(content) - 1:
                if indexes[0] == 0:
                    if (line[indexes[-1] + 1] not in collection or
                            check(i - 1, indexes[0] - 1, indexes[-1] + 1)):

                        number = ''

                        for idx in indexes:
                            number += line[idx]

                        res += int(number)

                elif indexes[-1] == len(line) - 2:
                    if (line[indexes[0] - 1] not in collection or
                            check(i - 1, indexes[0] - 1, indexes[-1] + 1)):

                        number = ''

                        for idx in indexes:
                            number += line[idx]

                        res += int(number)

                else:
                    if (line[indexes[-1] + 1] not in collection or
                            line[indexes[0] - 1] not in collection or
                            check(i - 1, indexes[0] - 1, indexes[-1] + 1)):

                        number = ''

                        for idx in indexes:
                            number += line[idx]

                        res += int(number)

            else:
                if indexes[0] == 0:
                    if (line[indexes[-1] + 1] not in collection or
                       check(i - 1, indexes[0] - 1, indexes[-1] + 1) or
                       check(i + 1, indexes[0] - 1, indexes[-1] + 1)):

                        number = ''

                        for idx in indexes:
                            number += line[idx]

                        res += int(number)

                elif indexes[-1] == len(line) - 2:
                    if (line[indexes[0] - 1] not in collection or
                       check(i - 1, indexes[0] - 1, indexes[-1] + 1) or
                       check(i + 1, indexes[0] - 1, indexes[-1] + 1)):

                        number = ''

                        for idx in indexes:
                            number += line[idx]

                        res += int(number)

                else:
                    if (line[indexes[-1] + 1] not in collection or
                       line[indexes[0] - 1] not in collection or
                       check(i - 1, indexes[0] - 1, indexes[-1] + 1) or
                       check(i + 1, indexes[0] - 1, indexes[-1] + 1)):

                        number = ''

                        for idx in indexes:
                            number += line[idx]

                        res += int(number)

            print(res)
        j += 1

print(content[0][5: 10] in collection)

print(res)
