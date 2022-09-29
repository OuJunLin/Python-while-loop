a, b = map(int, input().split())
if a < b:
    a, b = b, a
    
result_1 = 0
result_2 = 0

#輾轉相除法
d1 = a
d2 = b
r = d1%d2
while r != 0:
    d1 = d2
    d2 = r
    r = d1%d2

result_1 = d2
result_2 = result_1*(a/result_1)*(b/result_1)
print(result_1, "{:.0f}" .format(result_2), sep="\n")
