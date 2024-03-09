file = open("input.txt", 'r')

num_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
res = 0

for line in file.readlines():
    first = [len(line), -1]
    last = [-1, -1]

    for word in num_dict:
        first_word_index = line.find(word)
        last_word_index = line.rfind(word)

        if first_word_index != -1:
            if first_word_index < first[0]:
                first = [first_word_index, num_dict[word]]

        if last_word_index != -1:
            if last_word_index > last[0]:
                last = [last_word_index, num_dict[word]]

    for i in range(len(line)):

        if line[i].isdigit():
            if i < first[0]:
                first = [i, int(line[i])]

            if i > last[0]:
                last = [i, int(line[i])]

    res += first[1] * 10 + last[1]

file.close()

print(res)