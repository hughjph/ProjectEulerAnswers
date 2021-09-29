import string

fileObj = open("names.txt", "r")
words = fileObj.read().split(',')
fileObj.close()

for i in range(len(words)):
    words[i] = words[i].replace('\"', '')

words.sort()

total = 0

alphabet = list(string.ascii_uppercase)

for i in range(len(words)):
    print(words[i])
    sum_of_characters = 0
    for j in range(len(words[i])):
        sum_of_characters += ord(words[i][j]) - 64
    total += (sum_of_characters * (i+1))

print(total)