file = open("input.txt", 'r')
res = 0

for line in file.readlines():
    first = -1
    last = -1

    for i in range(len(line)):

        if line[i].isdigit():
            if first == -1:
                first = int(line[i])

            last = int(line[i])

    res += first * 10 + last

file.close()

print(res)




