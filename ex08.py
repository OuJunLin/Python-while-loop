n = int(input())
i = 1
j = 1
result = 1
count1 = 0

while i <= n:
    result *= i
    i += 1

while result%(j*10) == 0:
    j *= 10
    count1 += 1 
print(count1)