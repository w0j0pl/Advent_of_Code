import string

file = open("input.txt", 'r')
res = 0

for index, line in enumerate(file.readlines()):
    words = [word.strip(string.punctuation) for word in line.split() if word.strip(string.punctuation).isalnum()]
    dict = {}

    for i in range(2, len(words), 2):
        if words[i + 1] not in dict or int(dict[words[i + 1]]) < int(words[i]):
            dict[words[i + 1]] = int(words[i])

    if dict['red'] <= 12 and dict['green'] <= 13 and dict['blue'] <= 14:
        res += index + 1

print(res)
