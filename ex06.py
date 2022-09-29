n = input()
i = 0
sum1 = 0

while i < len(n):
    sum1 += int(n[i])
    i += 1

print(i, sum1, sep="\n")