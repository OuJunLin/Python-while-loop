n = int(input())
i = 2
flat = True

while i < n:
    if n%i == 0:
        flat = False
        break
    else:
        i +=1
if n == 1:
    flat = False

if flat == True:
    print("YES")
else:
    print("NO")