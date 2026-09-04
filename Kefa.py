n = int(input())

ia = input().split()
for i in range(n):
    ia[i] = int(ia[i])

pre = 0
cur = 1

start = ia[0]
for i in ia[1:]:
    if start <= i:
        cur+=1
        start = i
    else:
        if pre<cur:
            pre = cur
        cur = 1
        start = i

if pre>cur:
    fin = pre
else:
    fin = cur

print(fin)
