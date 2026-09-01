n = int(input())

b = 0
for i in range(n):
    e = input().split()
    a = 0
    for i in e:
        if int(i) == 1:
            a+=1
        else:
            continue 

    if a>=2:
        b +=1
    else:
        continue

print(b)

    
