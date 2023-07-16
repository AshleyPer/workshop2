import sys

words = sys.stdin.readlines()

total = 0

for word in words:
    word2 = word.split(' ')
    total = total + int(word2[1])

for word in words:
    word2 = word.split(' ')

    print(word2[0] , f"\t\t[{(int(word2[1]) * '#') * 2}] {int((int(word2[1]) / total) * 100)}%")
