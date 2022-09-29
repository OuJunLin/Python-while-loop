n = int(input())
i = 1
j = 1
sum_list = []
sum_tem = 0
flat = False

while i < n:
    j = i
    while sum_tem < n:
       sum_tem += j
       sum_list.append(str(j))
       j += 1
    if sum_tem == n:
        print("+".join(sum_list))
        flat = True
    sum_list = []
    sum_tem = 0
    i += 1

if flat == False:
    print("NO")