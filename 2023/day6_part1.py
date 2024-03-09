file = open("input.txt", 'r')
content = file.readlines()
file.close()

res = 1

times = []
distances = []

number = ''
for i, line in enumerate(content):
    for ch in line:
        if ch.isdigit():
            number += ch
        else:
            if number != '':
                if i == 0:
                    times.append(int(number))
                else:
                    distances.append(int(number))
                number = ''

if number != '':
    distances.append(int(number))

count = 0
for i, time in enumerate(times):
    for j in range(1, time):
        if j * (time - j) > distances[i]:
            count += 1
    res *= count
    count = 0

print(res)
