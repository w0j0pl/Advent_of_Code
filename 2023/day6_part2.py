file = open("input.txt", 'r')
content = file.readlines()
file.close()

res = 1

number = ''
for i, line in enumerate(content):
    for ch in line:
        if ch.isdigit():
            number += ch

    if i == 0:
        time = int(number)
    else:
        distance = int(number)

    number = ''

count = 0

for i in range(time):
    if i * (time - i) > distance:
        count += 1

print(count)
