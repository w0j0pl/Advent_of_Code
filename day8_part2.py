file = open("input.txt", 'r')

content = file.readlines()

file.close()

instruction = ''
for ch in content[0]:
    if ch.isalpha():
        instruction += ch

node = ''
temp_nodes = []
nodes = {}
A_nodes = []
is_A_node = False

for i in range(2, len(content)):
    for ch in content[i]:
        if ch.isalpha():
            node += ch
        else:
            if node != '':
                if len(temp_nodes) == 0 and node[-1] == 'A':
                    is_A_node = True
                temp_nodes.append(node)
                node = ''
    nodes[temp_nodes[0]] = (tuple(temp_nodes[1:]))
    if is_A_node:
        A_nodes.append(temp_nodes[0])
        is_A_node = False
    temp_nodes = []

map = {'L': 0, 'R': 1}
step_nodes = A_nodes

for j, step in enumerate(step_nodes):
    i = 0
    res = 0
    while True:
        step = nodes[step][map[instruction[i]]]

        res += 1
        i += 1
        if i == len(instruction):
            i = 0

        if step[2] == 'Z':
            print(res)
            break

