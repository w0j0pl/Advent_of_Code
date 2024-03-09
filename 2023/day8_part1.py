from functools import cache

file = open("input.txt", 'r')

content = file.readlines()

file.close()

instruction = ''
for ch in content[0]:
    if ch.isalpha():
        instruction += ch
print(instruction)

node = ''
temp_nodes = []
nodes = {}

for i in range(2, len(content)):
    for ch in content[i]:
        if ch.isalpha():
            node += ch
        else:
            if node != '':
                temp_nodes.append(node)
                node = ''
    nodes[temp_nodes[0]] = (tuple(temp_nodes[1:]))
    temp_nodes = []

map = {'L': 0, 'R': 1}
step = nodes['AAA']
i = 0
res = 0
while res < 10000000 and step != nodes['ZZZ']:
    step = nodes[step[map[instruction[i]]]]
    res += 1
    i += 1
    if i == len(instruction):
        i = 0

print(res)

